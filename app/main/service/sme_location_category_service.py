import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.sme_location_category import *


def save_new_sme_location_category(data):
    sme_location_category = SmeLocationCategory.query.filter_by(name=data['name']).first()
    if not sme_location_category:
        new_sme_location_category = SmeLocationCategory(
            name=data['name']
        )
        save_changes(new_sme_location_category)
        return generate_token(new_sme_location_category)

    else:
        response_object = {
            'status': 'fail',
            'message': 'Sme Location Category already exists. Please Log in.'
        }
        return response_object, 409


def get_all_sme_location_categories():
    return SmeLocationCategory.query.all()


def get_a_sme_location_category(id):
    return SmeLocationCategory.query.get_or_404(id)


def generate_token(sme_location_category):
    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'data': {
                'sme_tier_id': sme_location_category.id,
                'name': sme_location_category.name
                }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_sme_location_category(id):
    sme_location_category = get_a_sme_location_category(id)
    db.session.delete(sme_location_category)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Sme Location Category Successfully deleted.'
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


