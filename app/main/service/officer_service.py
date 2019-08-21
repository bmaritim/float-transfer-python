import uuid
import os
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.officer import Officer


def save_new_officer(data):
    officer = Officer.query.filter_by(email=data['email']).first()
    if not officer:
        new_officer = Officer(
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
            status_type=data['status_type'],
            photo=data['photo'],
            gender=data['gender'],
            password=data['password'],
            account=data['account']
        )
        save_changes(new_officer)
        return generate_new_officer(new_officer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'officer already exists.'
        }
        return response_object, 409


def get_all_officers():
    return Officer.query.all()


def get_an_officer(officer_id):
    return Officer.query.get_or_404(officer_id)


def generate_new_officer(officer):
    try:
        response_object = {
            'status': 'success',
            'message': 'Officer Successfully registered.',
            'data': {
                'officer_id': officer.id,
                'status_type': officer.status_type,
                'first_name': officer.first_name,
                'middle_name': officer.middle_name,
                'last_name': officer.last_name,
                'account': officer.account,
                'district': officer.district_id,
                'gender': officer.gender,
                'country': officer.country_id,
                'photo': officer.photo,
                'phone': officer.phone,
                'birth': officer.birth,
                'password': officer.password_hash,
                'email': officer.email,
                'town': officer.town_id,
                'state': officer.state
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_officer(officer_id, data):
    officer = Officer.query.filter_by(id=officer_id).first()
    if not officer:
        response_object = {
            'status': 'fail',
            'message': 'officer does not exist.'
        }
        return response_object, 409
    else:
        officer.email = officer.email
        officer.first_name = data['first_name']
        officer.middle_name = data['middle_name']
        officer.last_name = data['last_name']
        officer.phone = data['phone']
        officer.birth = data['birth']
        officer.state = data['state']
        officer.town_id = data['town_id']
        officer.country_id = data['country_id']
        officer.district_id = data['district_id']
        officer.status_type = data['status_type']
        officer.photo = data['photo']
        officer.gender = data['gender']
        officer.password = officer.password_hash
        officer.account = data['account']
        officer.deployed_town_id = data['deployed_town_id']
        officer.deployed_country_id = data['deployed_country_id']
        officer.deployed_district_id = data['deployed_district_id']
        db.session.commit()
        return update_officer(officer)


def update_officer(officer):
    try:
        response_object = {
            'status': 'success',
            'message': 'Officer Details Successfully updated.',
            'data': {
                'officer_id': officer.id,
                'status_type': officer.status_type,
                'first_name': officer.first_name,
                'middle_name': officer.middle_name,
                'last_name': officer.last_name,
                'account': officer.account,
                'district': officer.district_id,
                'gender': officer.gender,
                'country': officer.country_id,
                'photo': officer.photo,
                'phone': officer.phone,
                'birth': officer.birth,
                'password': officer.password_hash,
                'email': officer.email,
                'town': officer.town_id,
                'state': officer.state,
                'deployed_country': officer.deployed_country_id,
                'deployed_district': officer.deployed_district_id,
                'deployed_town': officer.deployed_town_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_officer(officer_id):
    officer = get_an_officer(officer_id)
    db.session.delete(officer)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Officer Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def deploy_an_officer(officer_id, data):
    officer = Officer.query.filter_by(id=officer_id).first()
    if not officer:
        response_object = {
            'status': 'fail',
            'message': 'officer not found.'
        }
        return response_object, 404
    elif officer.status_type is "DEPLOYED":
        response_object = {
            'status': 'fail',
            'message': 'officer already DEPLOYED.'
        }
        return response_object, 409
    officer.status_type = "DEPLOYED"
    officer.deployed_town_id = data['deployed_town_id']
    officer.deployed_country_id = data['deployed_country_id']
    officer.deployed_district_id = data['deployed_district_id']
    db.session.commit()
    return update_officer(officer)


def suspend_an_officer(officer_id):
    officer = Officer.query.filter_by(id=officer_id).first()
    if not officer:
        response_object = {
            'status': 'fail',
            'message': 'officer not found.'
        }
        return response_object, 404
    elif officer.status_type is "SUSPENDED":
        response_object = {
            'status': 'fail',
            'message': 'officer already suspended.'
        }
        return response_object, 409
    elif officer.status_type is "DEFAULT":
        response_object = {
            'status': 'fail',
            'message': 'officer has to be deployed first for them to be suspended.'
        }
        return response_object, 409
    officer.status_type = "SUSPENDED"
    db.session.commit()
    return update_officer(officer)


def terminate_an_officer(officer_id):
    officer = Officer.query.filter_by(id=officer_id).first()
    if not officer:
        response_object = {
            'status': 'fail',
            'message': 'officer not found.'
        }
        return response_object, 404
    elif officer.status_type is "TERMINATED":
        response_object = {
            'status': 'fail',
            'message': 'officer already terminated.'
        }
        return response_object, 409
    officer.status_type = "TERMINATED"
    db.session.commit()
    return update_officer(officer)


def save_changes(data):
    db.session.add(data)
    db.session.commit()


