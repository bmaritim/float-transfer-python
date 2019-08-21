import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.sme_user import SmeRole
from app.main.model.sme_permission import SmePermission


def save_new_sme_role(data):
    role = SmeRole.query.filter_by(name=data['name']).first()
    if not role:
        new_role = SmeRole(
            name=data['name']
        )
        permission = SmePermission(role=new_role)
        save_changes(new_role)
        return generate_new_sme_role(new_role)
    else:
        response_object = {
            'status': 'fail',
            'message': 'role already exists.'
        }
        return response_object, 409


def get_all_sme_roles():
    return SmeRole.query.all()


def get_a_sme_role(role_id):
    return SmeRole.query.get_or_404(role_id)


def generate_new_sme_role(role):
    try:
        response_object = {
            'status': 'success',
            'message': 'Role Successfully Created.',
            'data': {
                'id': role.id,
                'name': role.name
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_sme_role_permissions(role_id, data):
    role = SmeRole.query.get_or_404(role_id)
    role.from_dict(data)
    role.permissions.from_dict(data['permissions'])
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Role Successfully Edited.',
        'data': data
    }
    return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()

