import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._upload import Upload


def save_new_upload(data):
    upload = Upload.query.filter_by(up_title=data['up_title']).first()
    if not upload:
        new_upload = Upload(
            up_title=data['up_title'],
            up_poster=data['up_poster'],
            up_desc=data['up_desc'],
            up_attach=data['up_attach'],
            up_status=data['up_status'],
            category_id=data['category_id']
        )
        save_changes(new_upload)
        return generate_new_upload(new_upload)
    else:
        response_object = {
            'status': 'fail',
            'message': 'upload already exists.'
        }
        return response_object, 409


def get_all_uploads():
    return Upload.query.all()


def get_a_upload(upload_id):
    return Upload.query.get_or_404(upload_id)


def generate_new_upload(upload):
    try:
        response_object = {
            'status': 'success',
            'message': 'upload Successfully registered.',
            'data': {
                'id': upload.id,
                'up_title': upload.up_title,
                'up_poster': upload.up_poster,
                'up_desc': upload.up_desc,
                'up_attach': upload.up_attach,
                'up_status': upload.up_status,
                'category_id': upload.category_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_upload(upload_id, data):
    upload = Upload.query.filter_by(id=upload_id).first()
    if not upload:
        response_object = {
            'status': 'fail',
            'message': 'upload does not exist.'
        }
        return response_object, 409
    else:
        upload.up_title = data['up_title'],
        upload.up_poster = data['up_poster'],
        upload.up_desc = data['up_desc'],
        upload.up_attach = data['up_attach'],
        upload.up_status = data['up_status'],
        upload.category_id = data['category_id']
        db.session.commit()
        return update_upload(upload)


def update_upload(upload):
    try:
        response_object = {
            'status': 'success',
            'message': 'upload Details Successfully updated.',
            'data': {
                'id': upload.id,
                'up_title': upload.up_title,
                'up_poster': upload.up_poster,
                'up_desc': upload.up_desc,
                'up_attach': upload.up_attach,
                'up_status': upload.up_status,
                'category_id': upload.category_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_upload(upload_id):
    upload = get_a_upload(upload_id)
    db.session.delete(upload)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'upload Successfully deleted.'
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


