import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.mf import Mf
from json import dumps


def save_new_mf(data):
    mf = Mf.query.filter_by(email=data['email']).first()
    if not mf:
        new_mf = Mf(
            email=data['email'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            birth=data['birth'],
            state=data['state'],
            town_id=data['town_id'],
            country_id=data['country_id'],
            district_id=data['district_id'],
            mf_status_type=data['mf_status_type'],
            photo=data['photo'],
            gender=data['gender'],
            password=data['password'],
            account=data['account'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_mf)
        return generate_new_mf(new_mf)
    else:
        response_object = {
            'status': 'fail',
            'message': 'mf already exists.'
        }
        return response_object, 409


def get_all_mfs():
    return Mf.query.all()


def get_an_mf(mf_id):
    return Mf.query.get_or_404(mf_id)


def generate_new_mf(mf):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf Successfully registered.',
            'data': {
                'mf_id': mf.id,
                'mf_status_type': mf.mf_status_type,
                'first_name': mf.first_name,
                'middle_name': mf.middle_name,
                'last_name': mf.last_name,
                'account': mf.account,
                'district': mf.district_id,
                'gender': mf.gender,
                'country': mf.country_id,
                'photo': mf.photo,
                'phone': mf.phone,
                'birth': mf.birth,
                'password': mf.password_hash,
                'email': mf.email,
                'town': mf.town_id,
                'state': mf.state,
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_mf(mf_id, data):
    mf = Mf.query.filter_by(id=mf_id).first()
    if not mf:
        response_object = {
            'status': 'fail',
            'message': 'mf does not exist.'
        }
        return response_object, 409
    else:
        mf.email = mf.email
        mf.first_name = data['first_name']
        mf.middle_name = data['middle_name']
        mf.last_name = data['last_name']
        mf.phone = data['phone']
        mf.birth = data['birth']
        mf.state = data['state']
        mf.town_id = data['town_id']
        mf.country_id = data['country_id']
        mf.district_id = data['district_id']
        mf.mf_status_type = data['status_type']
        mf.photo = data['photo']
        mf.gender = data['gender']
        mf.password = mf.password_hash
        mf.account = data['account']
        mf.deployed_town_id = data['deployed_town_id']
        mf.deployed_country_id = data['deployed_country_id']
        mf.deployed_district_id = data['deployed_district_id']
        db.session.commit()
        return update_mf(mf)


def update_mf(mf):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf Details Successfully updated.',
            'data': {
                'mf_id': mf.id,
                'status_type': mf.mf_status_type,
                'first_name': mf.first_name,
                'middle_name': mf.middle_name,
                'last_name': mf.last_name,
                'account': mf.account,
                'district': mf.district_id,
                'gender': mf.gender,
                'country': mf.country_id,
                'photo': mf.photo,
                'phone': mf.phone,
                'birth': mf.birth,
                'password': mf.password_hash,
                'email': mf.email,
                'town': mf.town_id,
                'state': mf.state,
                'deployed_country': mf.deployed_country_id,
                'deployed_district': mf.deployed_district_id,
                'deployed_town': mf.deployed_town_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_mf(mf_id):
    mf = get_an_mf(mf_id)
    db.session.delete(mf)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'mf Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def deploy_an_mf(mf_id, data):
    mf = Mf.query.filter_by(id=mf_id).first()
    if not mf:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    elif mf.mf_status_type is "DEPLOYED":
        response_object = {
            'status': 'fail',
            'message': 'mf already DEPLOYED.'
        }
        return response_object, 409
    mf.mf_status_type = "DEPLOYED"
    mf.deployed_town_id = data['deployed_town_id']
    mf.deployed_country_id = data['deployed_country_id']
    mf.deployed_district_id = data['deployed_district_id']

    db.session.commit()
    return update_mf(mf)


def suspend_an_mf(mf_id):
    mf = Mf.query.filter_by(id=mf_id).first()
    if not mf:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    elif mf.mf_status_type is "SUSPENDED":
        response_object = {
            'status': 'fail',
            'message': 'mf already suspended.'
        }
        return response_object, 409
    elif mf.mf_status_type is "DEFAULT":
        response_object = {
            'status': 'fail',
            'message': 'mf has to be deployed first for them to be suspended.'
        }
        return response_object, 409
    mf.mf_status_type = "SUSPENDED"
    db.session.commit()
    return update_mf(mf)


def terminate_an_mf(mf_id):
    mf = Mf.query.filter_by(id=mf_id).first()
    if not mf:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    elif mf.mf_status_type is "TERMINATED":
        response_object = {
            'status': 'fail',
            'message': 'mf already terminated.'
        }
        return response_object, 409
    mf.mf_status_type = "TERMINATED"
    db.session.commit()
    return update_mf(mf)


def get_an_mf_deposit(mf_id):
    mf = Mf.query.filter_by(id=mf_id).first()
    if not mf:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    try:
        response_object = {
            'status': 'success',
            'message': 'mf deposits Successfully fetched.',
            'mf_deposits': ''
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()


