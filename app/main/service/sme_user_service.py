import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model import SmeUser


def save_new_sme_user(data):
    sme_user = SmeUser.query.filter_by(email=data['email']).first()
    if not sme_user:
        new_sme_user = SmeUser(
            role_id=2,
            email=data['email'],
            registered_on=datetime.datetime.utcnow(),
            public_id=str(uuid.uuid4()),
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            date_of_birth=data['date_of_birth'],
            address=data['address'],
            city=data['city'],
            country=data['country'],
            zip_code=data['zip_code'],
            status=data['status'],
            gender=data['gender'],
            national_id=data['national_id'],
            user_role='admin'
        )
        db.session.add(new_sme_user)
        db.session.commit()
        return generate_token(new_sme_user)

    else:
        response_object = {
            'status': 'fail',
            'message': 'Sme User already exists. Please Log in.'
        }
        return response_object, 409


def get_all_sme_users():
    return SmeUser.query.all()


def get_a_sme_user(id):
    return SmeUser.query.get_or_404(id)


def generate_token(sme_user):
    try:
        # generate the auth token
        auth_token = SmeUser.encode_auth_token(sme_user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode(),
            'data': {
                'user_id': sme_user.id,
                'status': sme_user.status,
                'first_name': sme_user.first_name,
                'last_name': sme_user.last_name,
                'public_id': sme_user.public_id,
                'gender': sme_user.gender,
                'country': sme_user.country,
                'national_id': sme_user.national_id,
                'phone': sme_user.phone,
                'date_of_birth': sme_user.date_of_birth,
                'address': sme_user.address,
                'password': sme_user.password_hash,
                'email': sme_user.email,
                'zip_code': sme_user.zip_code,
                'role': sme_user.role_id,
                'user_role': sme_user.user_role
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_sme_user(id):
    sme_user = get_a_sme_user(id)
    db.session.delete(sme_user)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Sme User Successfully deleted.'
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


