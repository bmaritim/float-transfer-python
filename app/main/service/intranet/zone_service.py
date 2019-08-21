import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._zone import Zone


def get_all_zones():
    return Zone.query.all()


def get_a_zone(zone_id):
    return Zone.query.get_or_404(zone_id)


def delete_a_zone(zone_id):
    zone = get_a_zone(zone_id)
    db.session.delete(zone)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'zone Successfully deleted.'
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


