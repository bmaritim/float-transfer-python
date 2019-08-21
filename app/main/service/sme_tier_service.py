import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.sme_tier import *


def save_new_sme_tier(data):
    sme_tier = SmeTier.query.filter_by(name=data['name']).first()
    if not sme_tier:
        new_sme_tier = SmeTier(
            name=data['name'],
            amount=data['amount']
        )
        save_changes(new_sme_tier)
        return generate_token(new_sme_tier)

    else:
        response_object = {
            'status': 'fail',
            'message': 'Sme Tier already exists. Please Log in.'
        }
        return response_object, 409


def get_all_sme_tiers():
    return SmeTier.query.all()


def get_a_sme_tier(id):
    return SmeTier.query.get_or_404(id)


def generate_token(sme_tier):
    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'data': {
                'sme_tier_id': sme_tier.id,
                'name': sme_tier.name,
                'amount': sme_tier.amount
                }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_sme_tier(id):
    sme_tier = get_a_sme_tier(id)
    db.session.delete(sme_tier)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Sme Tier Successfully deleted.'
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


