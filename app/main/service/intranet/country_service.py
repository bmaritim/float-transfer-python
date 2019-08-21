import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._country import Country


def get_all_countries():
    return Country.query.all()


def get_a_country(country_id):
    return Country.query.get_or_404(country_id)


def delete_a_country(country_id):
    country = get_a_country(country_id)
    db.session.delete(country)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'country Successfully deleted.'
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


