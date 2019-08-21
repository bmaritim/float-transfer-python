import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.country import Country


def save_new_country(data):
    country = Country.query.filter_by(name=data['name']).first()
    if not country:
        new_country = Country(
            name=data['name']
        )
        save_changes(new_country)
        return generate_new_country(new_country)
    else:
        response_object = {
            'status': 'fail',
            'message': 'country already exists.',
            'data': data
        }
        return response_object, 409


def get_all_countries():
    return Country.query.all()


def get_a_country(country_id):
    return Country.query.get_or_404(country_id)


def generate_new_country(country):
    try:
        response_object = {
            'status': 'success',
            'message': 'country Successfully registered.',
            'data': {
                'id': country.id,
                'name': country.name
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_country(country_id):
    country = get_a_country(country_id)
    db.session.delete(country)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Country Successfully deleted.'
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

