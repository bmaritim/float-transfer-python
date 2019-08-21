import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.mf_credit import MfCredit


def save_new_mf_credit(data):
        new_mf_credit = MfCredit(
            credit_date=data['credit_date'],
            credit_fees_configs_id=data['credit_fees_configs_id'],
            mf_id=data['mf_id']
        )
        save_changes(new_mf_credit)
        return generate_new_mf_credit(new_mf_credit)


def get_all_mf_credits():
    return MfCredit.query.all()


def get_all_mf_credits_by_mf(mf_id):
    return MfCredit.query.filter_by(mf_id=mf_id).all()


def get_an_mf_credit(mf_credit_id):
    return MfCredit.query.get_or_404(mf_credit_id)


def generate_new_mf_credit(mf_credit):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_credit Successfully registered.',
            'data': {
                'mf_credit_id': mf_credit.id,
                'credit_date': mf_credit.credit_date,
                'credit_fees_configs_id': mf_credit.credit_fees_configs_id,
                'credited_mf': mf_credit.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_mf_credit(mf_credit_id, data):
    mf_credit = MfCredit.query.filter_by(id=mf_credit_id).first()
    if not mf_credit:
        response_object = {
            'status': 'fail',
            'message': 'mf_credit does not exist.'
        }
        return response_object, 409
    else:
        mf_credit.penalty_date = data['penalty_date']
        mf_credit.mf_credit_fee_id = data['mf_credit_fee']
        db.session.commit()
        return update_mf_credit(mf_credit)


def update_mf_credit(mf_credit):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_credit Details Successfully updated.',
            'data': {
                'mf_credit_id': mf_credit.id,
                'credit_date': mf_credit.credit_date,
                'credit_fees_configs_id': mf_credit.credit_fees_configs_id,
                'credited_mf': mf_credit.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_mf_credit(mf_credit_id):
    mf_credit = get_an_mf_credit(mf_credit_id)
    db.session.delete(mf_credit)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_credit_deposit Successfully deleted.'
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


