import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._box import Box


def save_new_box(data):
    box = Box.query.filter_by(box_name=data['box_name']).first()
    if not box:
        new_box = Box(
            box_name=data['box_name'],
            box_mac=data['box_mac'],
            box_folder=data['box_folder'],
            location=data['location'],
            city=data['city'],
            zone_id=data['zone_id'],
            box_status=data['box_status'],
            country_id=data['country_id']
        )
        save_changes(new_box)
        return generate_new_box(new_box)
    else:
        response_object = {
            'status': 'fail',
            'message': 'box already exists.'
        }
        return response_object, 409


def get_all_boxes():
    return Box.query.all()


def get_a_box(box_id):
    return Box.query.get_or_404(box_id)


def generate_new_box(box):
    try:
        response_object = {
            'status': 'success',
            'message': 'box Successfully registered.',
            'data': {
                'box_name': box.box_name,
                'box_mac': box.box_mac,
                'box_folder': box.box_folder,
                'location': box.location,
                'city': box.city,
                'zone_id': box.zone_id,
                'country_id': box.country_id,
                'box_status': box.box_status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_box(box_id, data):
    box = Box.query.filter_by(id=box_id).first()
    if not box:
        response_object = {
            'status': 'fail',
            'message': 'box does not exist.'
        }
        return response_object, 409
    else:
        box.box_name = data['box_name'],
        box.box_mac = data['box_mac'],
        box.box_folder = data['box_folder'],
        box.location = data['location'],
        box.city = data['city'],
        box.zone_id = data['zone_id'],
        box.box_status = data['box_status'],
        box.country_id = data['country_id']
        db.session.commit()
        return update_box(box)


def update_box(box):
    try:
        response_object = {
            'status': 'success',
            'message': 'box Details Successfully updated.',
            'data': {
                'box_name': box.box_name,
                'box_mac': box.box_mac,
                'box_folder': box.box_folder,
                'location': box.location,
                'city': box.city,
                'zone_id': box.zone_id,
                'country_id': box.country_id,
                'box_status': box.box_status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_box(box_id):
    box = get_a_box(box_id)
    db.session.delete(box)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'box Successfully deleted.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()


