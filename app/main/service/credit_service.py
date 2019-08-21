import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.therest import CreditFeeConfig


def save_new_credit(data):
    new_credit = CreditFeeConfig(
        fee=data['fee'],
        amount=data['amount'],
        approval=data['approval_req']
    )
    save_changes(new_credit)
    return generate_new_credit(new_credit)


def get_all_credits():
    return CreditFeeConfig.query.all()


def get_an_credit(credit_id):
    return CreditFeeConfig.query.get_or_404(credit_id)


def generate_new_credit(credit):
    try:
        response_object = {
            'status': 'success',
            'message': 'credit Successfully registered.',
            'data': {
                'credit_id': credit.id,
                'fee': credit.fee,
                'amount': credit.amount,
                'approval': credit.approval_req,
                'status': credit.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_credit(credit_id, data):
    credit = CreditFeeConfig.query.filter_by(id=credit_id).first()
    if not credit:
        response_object = {
            'status': 'fail',
            'message': 'credit does not exist.'
        }
        return response_object, 409
    else:
        credit.fee = data['fee']
        credit.amount = data['amount']
        credit.approval_req = data['approval_req']
        db.session.commit()
        return update_credit(credit)


def update_credit(credit):
    try:
        response_object = {
            'status': 'success',
            'message': 'credit Details Successfully updated.',
            'data': {
                'credit_id': credit.id,
                'fee': credit.fee,
                'amount': credit.amount,
                'approval': credit.approval_req,
                'status': credit.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_credit(credit_id):
    credit = get_an_credit(credit_id)
    db.session.delete(credit)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'credit Successfully deleted.'
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


