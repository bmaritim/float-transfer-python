import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.district import District


def save_new_district(data):
    district = District.query.filter_by(name=data['name']).first()
    if not district:
        new_district = District(
            name=data['name'],
            country_id=data['country_id']
        )
        save_changes(new_district)
        return generate_new_district(new_district)
    else:
        response_object = {
            'status': 'fail',
            'message': 'district already exists.',
            'data': data
        }
        return response_object, 409


def get_all_districts():
    return District.query.all()


def get_a_district(district_id):
    return District.query.get_or_404(district_id)


def generate_new_district(district):
    try:
        response_object = {
            'status': 'success',
            'message': 'district Successfully registered.',
            'data': {
                'id': district.id,
                'name': district.name,
                'country': district.country.name
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

