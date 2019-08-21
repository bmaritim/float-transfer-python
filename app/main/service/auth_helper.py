import os
from app.main.model.user import User
from app.main.model.officer import Officer
from ..service.blacklist_service import save_token
from flask_mail import Mail, Message
from app.main import mail
from threading import Thread
from random import *
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

otp = randint(000000, 999999)


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            officer = Officer.query.filter_by(email=data.get('email')).first()

            if user and user.check_password(data.get('password')) or officer and\
                    officer.check_password(data.get('password')):
                if user:
                    auth_token = User.encode_auth_token(user.id)
                    if auth_token:
                        msg = Message('OTP', sender='mshiriki.otp@gmail.com', recipients=[(data.get('email'))])
                        msg.body = str(otp)
                        msg.html = '<div style="border: 1px solid #186a27; width: 600px;"> <div style="background-color: #e0f5e6; padding: 15px;"> <img src="https://res.cloudinary.com/pascalnjue/image/upload/v1558445433/logo_mxfwdy.png" /> </div> <div style="padding: 15px;"> <p> Dear {0}, <br> <br> You are trying to login on M-SHIRIKI\'s admin application and for the security purpose it is required to enter the OTP. This OTP is valid only for next 10 minutes. To continue your login with this session please enter the OTP {1}. <br> <br> Best Regards, <br> M-SHIRIKI. <br> <br> Copyright 2019 M-SHIRIKI. All Rights Reserved. <p> </div></div>'.format(user.full_name(), msg.body)
                        thr = Thread(target=Auth.send_async_email, args=[app, msg])
                        thr.start()
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in. Proceed with OTP',
                            'Authorization': auth_token.decode(),
                            'id': user.id,
                            'role': user.role.name,
                            'otp': msg.body
                        }
                        return response_object, 200
                elif officer:
                    auth_token = Officer.encode_auth_token(officer.id)
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in',
                        'Authorization': auth_token.decode(),
                        'id': officer.id
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get("Authorization")
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                if user:
                    response_object = {
                        "status": "success",
                        "data": {
                            "id": user.id,
                            "email": user.email,
                            "admin": user.admin,
                            "role_id": user.role_id,
                            "role_name": user.role.name,
                            "registered_on": str(user.registered_on),
                            "status": user.status,
                            "city": user.city,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "public_id": user.public_id,
                            "amount_deposit": user.amount_deposit,
                            "district": user.district,
                            "gender": user.gender,
                            "country": user.country,
                            "image": user.image,
                            "tin_no": user.tin_no,
                            "national_id": user.national_id,
                            "description": user.description,
                            "phone": user.phone,
                            "date_of_birth": user.date_of_birth,
                            "address": user.address,
                            "business_name": user.business_name,
                            "password": user.password_hash,
                            "zip_code": user.zip_code,
                        },
                    }
                    return response_object, 200
                else:
                    resp = Officer.decode_auth_token(auth_token)
                    if not isinstance(resp, str):
                        officer = Officer.query.filter_by(id=resp).first()
                        if officer is None:
                            response_object = {
                                "status": "fail",
                                "message": "token expired. Please log in again.",
                            }
                            return response_object, 401
                        response_object = {
                            "status": "success",
                            "data": {
                                "id": officer.id,
                                "email": officer.email,
                                "first_name": officer.first_name,
                                "last_name": officer.last_name,
                            },
                        }
                        return response_object, 200
            response_object = {
                "status": "fail",
                "message": resp
            }
            return response_object, 401
    
    @staticmethod
    def send_async_email(app, msg):
        with app.app_context():
            mail.send(msg)

    @staticmethod
    def send_otp(email):
        msg = Message('OTP', sender='iroshbrian@gmail.com', recipients=[email])
        msg.body = str(otp)
        thr = Thread(target=Auth.send_async_email, args=[app, msg])
        thr.start()

        try:
            response_object = {
                'status': 'success',
                'message': 'Otp sent Successfully.',
                'data': msg.body
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 401

