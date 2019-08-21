import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.therest import LeasingFee


def save_new_leasing_fee(data):
    leasing_fee = LeasingFee.query.filter_by(name=data['name']).first()
    if not leasing_fee:
        new_leasing_fee = LeasingFee(
            applicable_from=data['applicable_from'],
            fee_amount=data['fee_amount']
        )
        save_changes(new_leasing_fee)
        return generate_new_leasing_fee(new_leasing_fee)
    else:
        response_object = {
            'status': 'fail',
            'message': 'leasing_fee already exists.',
            'data': data
        }
        return response_object, 409


def get_all_leasing_fees():
    return LeasingFee.query.all()


def get_a_leasing_fee(leasing_fee_id):
    return LeasingFee.query.get_or_404(leasing_fee_id)


def generate_new_leasing_fee(leasing_fee):
    try:
        response_object = {
            'status': 'success',
            'message': 'leasing_fee Successfully registered.',
            'data': {
                'id': leasing_fee.id,
                'applicable_from': leasing_fee.applicable_from,
                'fee_amount': leasing_fee.fee_amount
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_leasing_fee(leasing_fee_id, data):
    leasing_fee = LeasingFee.query.filter_by(id=leasing_fee_id).first()
    if not leasing_fee:
        response_object = {
            'status': 'fail',
            'message': 'mf_credit does not exist.'
        }
        return response_object, 409
    else:
        leasing_fee.leasing_fee_type = data['leasing_fee_type']
        leasing_fee.status = data['status']
        db.session.commit()
        return update_leasing_fee(leasing_fee)


def update_leasing_fee(leasing_fee):
    try:
        response_object = {
            'status': 'success',
            'message': 'payment mode Details Successfully updated.',
            'data': {
                'id': leasing_fee.id,
                'applicable_from': leasing_fee.applicable_from,
                'fee_amount': leasing_fee.fee_amount
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_leasing_fee(leasing_fee):
    leasing_fee = get_a_leasing_fee(leasing_fee)
    db.session.delete(leasing_fee)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Payment mode Successfully deleted.'
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

