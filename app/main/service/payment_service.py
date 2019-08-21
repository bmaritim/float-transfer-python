import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.therest import PaymentMode


def save_new_payment_mode(data):
    payment_mode = PaymentMode.query.filter_by(name=data['name']).first()
    if not payment_mode:
        new_payment_mode = PaymentMode(
            payment_mode_type=data['payment_mode_type'],
            status=data['status']
        )
        save_changes(new_payment_mode)
        return generate_new_payment_mode(new_payment_mode)
    else:
        response_object = {
            'status': 'fail',
            'message': 'payment_mode already exists.',
            'data': data
        }
        return response_object, 409


def get_all_payment_modes():
    return PaymentMode.query.all()


def get_a_payment_mode(payment_mode_id):
    return PaymentMode.query.get_or_404(payment_mode_id)


def generate_new_payment_mode(payment_mode):
    try:
        response_object = {
            'status': 'success',
            'message': 'payment_mode Successfully registered.',
            'data': {
                'id': payment_mode.id,
                'name': payment_mode.payment_mode_type,
                'status': payment_mode.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_payment_mode(payment_mode_id, data):
    payment_mode = PaymentMode.query.filter_by(id=payment_mode_id).first()
    if not payment_mode:
        response_object = {
            'status': 'fail',
            'message': 'mf_credit does not exist.'
        }
        return response_object, 409
    else:
        payment_mode.payment_mode_type = data['payment_mode_type']
        payment_mode.status = data['status']
        db.session.commit()
        return update_payment_mode(payment_mode)


def update_payment_mode(payment_mode):
    try:
        response_object = {
            'status': 'success',
            'message': 'payment mode Details Successfully updated.',
            'data': {
                'id': payment_mode.id,
                'name': payment_mode.payment_mode_type,
                'status': payment_mode.status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_payment_mode(payment_mode):
    payment_mode = get_a_payment_mode(payment_mode)
    db.session.delete(payment_mode)
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

