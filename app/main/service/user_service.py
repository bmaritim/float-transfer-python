import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.user import User, Role


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            date_of_birth=data['date_of_birth'],
            address=data['address'],
            city=data['city'],
            country=data['country'],
            zip_code=data['zip_code'],
            status=data['status'],
            business_name=data['business_name'],
            tin_no=data['tin_no'],
            image=data['image'],
            amount_deposit=data['amount_deposit'],
            description=data['description'],
            gender=data['gender'],
            district=data['district'],
            national_id=data['national_id'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow(),
            role_id=data['role_id']
        )
        save_changes(new_user)
        return generate_token(new_user)

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.get_or_404(id)


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode(),
            'data': {
                'user_id': user.id,
                'status': user.status,
                'city': user.city,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'public_id': user.public_id,
                'amount_deposit': user.amount_deposit,
                'district': user.district,
                'gender': user.gender,
                'country': user.country,
                'image': user.image,
                'tin_no': user.tin_no,
                'national_id': user.national_id,
                'description': user.description,
                'phone': user.phone,
                'date_of_birth': user.date_of_birth,
                'address': user.address,
                'business_name': user.business_name,
                'password': user.password_hash,
                'email': user.email,
                'zip_code': user.zip_code,
                'role': user.user_role,
                'role_id': user.role_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_user(id):
    user = get_a_user(id)
    db.session.delete(user)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'User Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()


