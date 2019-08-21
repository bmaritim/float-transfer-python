import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._user import IUser


def save_new_i_user(data):
    i_user = IUser.query.filter_by(email=data['email']).first()
    if not i_user:
        new_i_user = IUser(
            name=data['name'],
            utype_id=data['utype_id'],
            client_id=data['client_id'],
            email=data['email'],
            password=data['password'],
            user_status=data['user_status']
        )
        db.session.add(new_i_user)
        db.session.commit()
        return generate_token(new_i_user)

    else:
        response_object = {
            'status': 'fail',
            'message': 'Intranet User already exists. Please Log in.'
        }
        return response_object, 409


def get_all_i_users():
    return IUser.query.all()


def get_a_i_user(i_user_id):
    return IUser.query.get_or_404(i_user_id)


def generate_token(i_user):
    try:
        # generate the auth token
        auth_token = IUser.encode_auth_token(i_user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode(),
            'data': {
                'user_id': i_user.id,
                'user_status': i_user.user_status,
                'name': i_user.name,
                'email': i_user.email
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_an_i_user(i_user_id, data):
    i_user = IUser.query.filter_by(id=i_user_id).first()
    if not i_user:
        response_object = {
            'status': 'fail',
            'message': 'mf_deposit does not exist.'
        }
        return response_object, 409
    else:
        i_user.name = data['name'],
        i_user.utype_id = data['utype_id'],
        i_user.client_id = data['client_id'],
        i_user.email = data['email'],
        i_user.password = data['password'],
        i_user.user_status = data['user_status']
        db.session.commit()
        return update_an_i_user(i_user)


def update_an_i_user(i_user):
    try:
        response_object = {
            'status': 'success',
            'message': 'Kiosk Successfully updated.',
            'data': {
                'user_id': i_user.id,
                'user_status': i_user.user_status,
                'name': i_user.name,
                'email': i_user.email
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_i_user(i_user_id):
    i_user = get_a_i_user(i_user_id)
    db.session.delete(i_user)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Int User Successfully deleted.'
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


