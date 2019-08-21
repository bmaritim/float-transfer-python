import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.town import Town


def save_new_town(data):
    town = Town.query.filter_by(name=data['name']).first()
    if not town:
        new_town = Town(
            name=data['name'],
            district_id=data['district_id']
        )
        save_changes(new_town)
        return generate_new_town(new_town)
    else:
        response_object = {
            'status': 'fail',
            'message': 'town already exists.',
            'data': data
        }
        return response_object, 409


def get_all_towns():
    return Town.query.all()


def get_a_town(town_id):
    return Town.query.get_or_404(town_id)


def generate_new_town(town):
    try:
        response_object = {
            'status': 'success',
            'message': 'town Successfully registered.',
            'data': {
                'id': town.id,
                'name': town.name,
                'district': town.district.name
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

