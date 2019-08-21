import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.mf_reimbursement import MfReimbursement


def save_new_mf_reimbursement(data):
    mf_reimbursement = MfReimbursement.query.filter_by(reference_number=data['reference_number']).first()
    if not mf_reimbursement:
        new_mf_reimbursement = MfReimbursement(
            reimbursement_date=data['reimbursement_date'],
            reimbursement_amount=data['reimbursement_amount'],
            payment_mode=data['payment_mode'],
            reference_number=data['reference_number'],
        )
        save_changes(new_mf_reimbursement)
        return generate_new_mf_reimbursement(new_mf_reimbursement)
    else:
        response_object = {
            'status': 'fail',
            'message': 'mf_reimbursement already exists.'
        }
        return response_object, 409


def get_all_mf_reimbursements():
    return MfReimbursement.query.all()


def get_all_mf_reimbursements_by_mf(mf_id):
    return MfReimbursement.query.filter_by(mf_id=mf_id).all()


def get_an_mf_reimbursement(mf_reimbursement_id):
    return MfReimbursement.query.get_or_404(mf_reimbursement_id)


def generate_new_mf_reimbursement(mf_reimbursement):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_reimbursement Successfully registered.',
            'data': {
                'mf_reimbursement_id': mf_reimbursement.id,
                'reimbursement_date': mf_reimbursement.reimbursement_date,
                'reimbursement_amount': mf_reimbursement.reimbursement_amount,
                'payment_mode': mf_reimbursement.payment_mode,
                'reference_number': mf_reimbursement.reference_number
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_mf_reimbursement(mf_reimbursement_id, data):
    mf_reimbursement = MfReimbursement.query.filter_by(id=mf_reimbursement_id).first()
    if not mf_reimbursement:
        response_object = {
            'status': 'fail',
            'message': 'mf_reimbursement does not exist.'
        }
        return response_object, 409
    else:
        mf_reimbursement.reimbursement_date = data['reimbursement_date']
        mf_reimbursement.reimbursement_amount = data['reimbursement_amount']
        mf_reimbursement.payment_mode = data['payment_mode']
        mf_reimbursement.reference_number = data['reference_number']
        db.session.commit()
        return update_mf_reimbursement(mf_reimbursement)


def update_mf_reimbursement(mf_reimbursement):
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_reimbursement Details Successfully updated.',
            'data': {
                'mf_reimbursement_id': mf_reimbursement.id,
                'reimbursement_date': mf_reimbursement.reimbursement_date,
                'reimbursement_amount': mf_reimbursement.reimbursement_amount,
                'payment_mode': mf_reimbursement.payment_mode,
                'reference_number': mf_reimbursement.reference_number
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_mf_reimbursement(mf_reimbursement_id):
    mf_reimbursement = get_an_mf_reimbursement(mf_reimbursement_id)
    db.session.delete(mf_reimbursement)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'mf_reimbursement_reimbursement Successfully deleted.'
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


