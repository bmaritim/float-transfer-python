import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.therest import MfPenaltyFee


def save_new_penalty(data):
    new_penalty = MfPenaltyFee(
        penalty_type=data['penalty_type'],
        charges=data['charges'],
        is_active=data['is_active']
    )
    save_changes(new_penalty)
    return generate_new_penalty(new_penalty)


def get_all_penalties():
    return MfPenaltyFee.query.all()


def get_an_penalty(penalty_id):
    return MfPenaltyFee.query.get_or_404(penalty_id)


def generate_new_penalty(penalty):
    try:
        response_object = {
            'status': 'success',
            'message': 'penalty Successfully registered.',
            'data': {
                'penalty_id': penalty.id,
                'penalty_type': penalty.penalty_type,
                'charges': penalty.charges,
                'is_active': penalty.is_active,
                'status': penalty.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_penalty(penalty_id, data):
    penalty = MfPenaltyFee.query.filter_by(id=penalty_id).first()
    if not penalty:
        response_object = {
            'status': 'fail',
            'message': 'penalty does not exist.'
        }
        return response_object, 409
    else:
        penalty.fee = data['fee']
        penalty.amount = data['amount']
        penalty.approval_req = data['approval_req']
        db.session.commit()
        return update_penalty(penalty)


def update_penalty(penalty):
    try:
        response_object = {
            'status': 'success',
            'message': 'penalty Details Successfully updated.',
            'data': {
                'penalty_id': penalty.id,
                'penalty_type': penalty.penalty_type,
                'charges': penalty.charges,
                'is_active': penalty.is_active,
                'status': penalty.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_penalty(penalty_id):
    penalty = get_an_penalty(penalty_id)
    db.session.delete(penalty)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'penalty Successfully deleted.'
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


