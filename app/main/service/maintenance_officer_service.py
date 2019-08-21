import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.maintenance_officer import MaintenanceOfficer


def save_new_maintenance_officer(data):
    maintenance_officer = MaintenanceOfficer.query.filter_by(email=data['email']).first()
    if not maintenance_officer:
        new_maintenance_officer = MaintenanceOfficer(
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
        save_changes(new_maintenance_officer)
        return generate_new_maintenance_officer(new_maintenance_officer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'maintenance officer already exists. Please Log in.',
            'data': data
        }
        return response_object, 409


def get_all_maintenance_officers():
    return MaintenanceOfficer.query.all()


def get_a_maintenance_officer(maintenance_officer_id):
    return MaintenanceOfficer.query.get_or_404(maintenance_officer_id)


def generate_new_maintenance_officer(maintenance_officer):
    try:
        response_object = {
            'status': 'success',
            'message': 'Maintenance Officer Successfully registered.',
            'data': {
                'maintenance_officer_id': maintenance_officer.id,
                'status_type': maintenance_officer.status_type,
                'first_name': maintenance_officer.first_name,
                'middle_name': maintenance_officer.middle_name,
                'last_name': maintenance_officer.last_name,
                'account': maintenance_officer.account,
                'district': maintenance_officer.district_id,
                'gender': maintenance_officer.gender,
                'country': maintenance_officer.country_id,
                'photo': maintenance_officer.photo,
                'phone': maintenance_officer.phone,
                'birth': maintenance_officer.birth,
                'password': maintenance_officer.password_hash,
                'email': maintenance_officer.email,
                'town': maintenance_officer.town_id,
                'state': maintenance_officer.state
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def update_maintenance_officer(maintenance_officer):
    try:
        response_object = {
            'status': 'success',
            'message': 'Maintenance Officer Details Successfully updated.',
            'data': {
                'maintenance_officer_id': maintenance_officer.id,
                'status_type': maintenance_officer.status_type,
                'first_name': maintenance_officer.first_name,
                'middle_name': maintenance_officer.middle_name,
                'last_name': maintenance_officer.last_name,
                'account': maintenance_officer.account,
                'district': maintenance_officer.district_id,
                'gender': maintenance_officer.gender,
                'country': maintenance_officer.country_id,
                'photo': maintenance_officer.photo,
                'phone': maintenance_officer.phone,
                'birth': maintenance_officer.birth,
                'password': maintenance_officer.password_hash,
                'email': maintenance_officer.email,
                'town': maintenance_officer.town_id,
                'state': maintenance_officer.state
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_maintenance_officer(officer_id):
    m_officer = get_a_maintenance_officer(officer_id)
    db.session.delete(m_officer)
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


def deploy_a_maintenance_officer(officer_id):
    m_officer = MaintenanceOfficer.query.filter_by(id=officer_id).first()
    if not m_officer:
        response_object = {
            'status': 'fail',
            'message': 'maintenance officer not found.'
        }
        return response_object, 404
    elif m_officer.status_type is "DEPLOYED":
        response_object = {
            'status': 'fail',
            'message': 'officer already DEPLOYED.'
        }
        return response_object, 409
    m_officer.status_type = "DEPLOYED"
    save_changes(m_officer)
    return update_maintenance_officer(m_officer)


def suspend_a_maintenance_officer(officer_id):
    m_officer = MaintenanceOfficer.query.filter_by(id=officer_id).first()
    if not m_officer:
        response_object = {
            'status': 'fail',
            'message': 'officer not found.'
        }
        return response_object, 404
    elif m_officer.status_type is "SUSPENDED":
        response_object = {
            'status': 'fail',
            'message': 'officer already suspended.'
        }
        return response_object, 409
    m_officer.status_type = "SUSPENDED"
    save_changes(m_officer)


def terminate_a_maintenance_officer(officer_id):
    m_officer = MaintenanceOfficer.query.filter_by(id=officer_id).first()
    if not m_officer:
        response_object = {
            'status': 'fail',
            'message': 'officer not found.'
        }
        return response_object, 404
    elif m_officer.status_type is "TERMINATED":
        response_object = {
            'status': 'fail',
            'message': 'officer already terminated.'
        }
        return response_object, 409
    m_officer.status_type = "TERMINMATED"
    save_changes(m_officer)


def save_changes(data):
    db.session.add(data)
    db.session.commit()

