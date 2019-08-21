import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.mf_penalty import MfPenalty


def save_new_mf_penalty(data):
        new_mf_penalty = MfPenalty(
            penalty_date=data['penalty_date'],
            mf_penalty_fee_id=data['mf_penalty_fee_id'],
            mf_id=data['mf_id']
        )
        save_changes(new_mf_penalty)
        return generate_new_mf_penalty(new_mf_penalty)


def get_all_mf_penalties():
    return MfPenalty.query.all()


def get_all_mf_penalties_by_mf(mf_id):
    return MfPenalty.query.filter_by(mf_id=mf_id).all()


def get_an_mf_penalty(mf_penalty_id):
    return MfPenalty.query.get_or_404(mf_penalty_id)


def generate_new_mf_penalty(mf_penalty):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_penalty Successfully registered.',
            'data': {
                'mf_penalty_id': mf_penalty.id,
                'penalty_date': mf_penalty.penalty_date,
                'penalty': mf_penalty.mf_penalty_fee_id,
                'penalised_mf': mf_penalty.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_mf_penalty(mf_penalty_id, data):
    mf_penalty = MfPenalty.query.filter_by(id=mf_penalty_id).first()
    if not mf_penalty:
        response_object = {
            'status': 'fail',
            'message': 'mf_penalty does not exist.'
        }
        return response_object, 409
    else:
        mf_penalty.penalty_date = data['penalty_date']
        mf_penalty.mf_penalty_fee_id = data['mf_penalty_fee']
        db.session.commit()
        return update_mf_penalty(mf_penalty)


def update_mf_penalty(mf_penalty):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_penalty Details Successfully updated.',
            'data': {
                'mf_penalty_id': mf_penalty.id,
                'penalty_date': mf_penalty.penalty_date,
                'penalty': mf_penalty.mf_penalty_fee_id,
                'penalised_mf': mf_penalty.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_mf_penalty(mf_penalty_id):
    mf_penalty = get_an_mf_penalty(mf_penalty_id)
    db.session.delete(mf_penalty)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_penalty_deposit Successfully deleted.'
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


