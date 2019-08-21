import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.mf_deposit import MfDeposit


def save_new_mf_deposit(data):
    mf_deposit = MfDeposit.query.filter_by(reference_number=data['reference_number']).first()
    if not mf_deposit:
        new_mf_deposit = MfDeposit(
            deposit_date=data['deposit_date'],
            deposit_amount=data['deposit_amount'],
            payment_mode=data['payment_mode'],
            reference_number=data['reference_number'],
            mf_id=data['mf_id']
        )
        save_changes(new_mf_deposit)
        return generate_new_mf_deposit(new_mf_deposit)
    else:
        response_object = {
            'status': 'fail',
            'message': 'mf_deposit already exists.'
        }
        return response_object, 409


def get_all_mf_deposits():
    return MfDeposit.query.all()


def get_all_mf_deposits_by_mf(mf_id):
    return MfDeposit.query.filter_by(mf_id=mf_id).all()


def get_an_mf_deposit(mf_deposit_id):
    return MfDeposit.query.get_or_404(mf_deposit_id)


def generate_new_mf_deposit(mf_deposit):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_deposit Successfully registered.',
            'data': {
                'mf_deposit_id': mf_deposit.id,
                'deposit_amount': mf_deposit.deposit_amount,
                'payment_mode': mf_deposit.payment_mode,
                'reference_number': mf_deposit.reference_number,
                'mf_id': mf_deposit.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_mf_deposit(mf_deposit_id, data):
    mf_deposit = MfDeposit.query.filter_by(id=mf_deposit_id).first()
    if not mf_deposit:
        response_object = {
            'status': 'fail',
            'message': 'mf_deposit does not exist.'
        }
        return response_object, 409
    else:
        mf_deposit.deposit_date = data['deposit_date']
        mf_deposit.deposit_amount = data['deposit_amount']
        mf_deposit.payment_mode = data['payment_mode']
        mf_deposit.reference_number = data['reference_number']
        db.session.commit()
        return update_mf_deposit(mf_deposit)


def update_mf_deposit(mf_deposit):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_deposit Details Successfully updated.',
            'data': {
                'mf_deposit_id': mf_deposit.id,
                'deposit_amount': mf_deposit.deposit_amount,
                'payment_mode': mf_deposit.payment_mode,
                'reference_number': mf_deposit.reference_number,
                'mf_id': mf_deposit.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_mf_deposit_by_mf_id(mf_id):
    return MfDeposit.query.filter_by(mf_id=mf_id).all()


def delete_an_mf_deposit(mf_deposit_id):
    mf_deposit = get_an_mf_deposit(mf_deposit_id)
    db.session.delete(mf_deposit)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_deposit_deposit Successfully deleted.'
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


