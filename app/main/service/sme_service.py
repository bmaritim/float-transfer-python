import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model import Sme


def save_new_sme(data):
    sme = Sme.query.filter_by(business_name=data['business_name']).first()
    if not sme:
        new_sme = Sme(
            business_name=data['business_name'],
            sme_status_type="PENDING",
            tin=data['tin'],
            sme_location_category=data['sme_location_category'],
            type_of_service=data['type_of_service'],
            sme_tier=data['sme_tier'],
            rdb_certificate=data['rdb_certificate'],
            tin_certificate=data['tin_certificate'],
            sme_compliance_cert=data['sme_compliance_cert'],
            id_copy=data['id_copy'],
            proof_of_payment=data['proof_of_payment'],
            country_id=data['country_id'],
            district_id=data['district_id'],
            town_id=data['town_id'],
        )
        save_changes(new_sme)
        return generate_token(new_sme)

    else:
        response_object = {
            'status': 'fail',
            'message': 'Sme already exists. Please Log in.'
        }
        return response_object, 409


def get_all_smes():
    return Sme.query.all()


def get_a_sme(id):
    return Sme.query.get_or_404(id)


def generate_token(sme):
    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'data': {
                'sme_id': sme.id,
                'business_name': sme.business_name,
                'sme_status_type': sme.sme_status_type,
                'tin': sme.tin,
                'sme_location_category': sme.sme_location_category,
                'type_of_service': sme.type_of_service,
                'sme_tier': sme.sme_tier,
                'rdb_certificate': sme.rdb_certificate,
                'tin_certificate': sme.tin_certificate,
                'sme_compliance_cert': sme.sme_compliance_cert,
                'id_copy': sme.id_copy,
                'proof_of_payment': sme.proof_of_payment,
                'country_id': sme.country_id,
                'district_id': sme.district_id,
                'town_id': sme.town_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_sme(id):
    sme = get_a_sme(id)
    db.session.delete(sme)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Sme Successfully deleted.'
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


