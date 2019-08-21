import uuid
import datetime
import os
from flask import json, jsonify, request, send_file, url_for
from app.main import db, create_app
from app.main.model.kiosk import Kiosk
import pyqrcode

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
basedir = os.path.dirname(app.instance_path)


def save_new_kiosk(data):
    kiosk = Kiosk.query.filter_by(model=data['model']).first()
    if not kiosk:
        new_kiosk = Kiosk(
            model=data['model'],
            purchase_date=data['purchase_date']
        )
        save_changes(new_kiosk)
        return generate_new_kiosk(new_kiosk)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Kiosk already exists.',
            'data': data
        }
        return response_object, 409


def get_all_kiosks():
    return Kiosk.query.all()


def get_a_kiosk(kiosk_id):
    return Kiosk.query.get_or_404(kiosk_id)


def generate_new_kiosk(kiosk):
    try:
        response_object = {
            'status': 'success',
            'message': 'Kiosk Successfully registered.',
            'data': {
                'id': kiosk.id,
                'model': kiosk.model
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def update_kiosk(kiosk):
    try:
        response_object = {
            'status': 'success',
            'message': 'Kiosk Successfully updated.',
            'data': {
                'id': kiosk.id,
                'model': kiosk.model,
                'mf_id': kiosk.mf_id,
                'condition': kiosk.condition
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def read_kiosk_qr(image):
    d = pyqrcode.Decoder()
    if d.decode(image):
        print('result: ' + d.result)
    else:
        print('error: ' + d.error)


def generate_kiosk_qr(kiosk_id):
    # Generate QR code
    url = pyqrcode.create(kiosk_id)
    url.svg("kioskqr{0}.svg".format(kiosk_id), scale=8)
    image_as_str = url.png_as_base64_str("kioskqr{0}.png".format(kiosk_id), scale=5)
    html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
    try:
        send_file(os.path.join(basedir, 'kioskqr{0}.svg'.format(kiosk_id)),
                  attachment_filename="kioskqr{0}.svg".format(kiosk_id)
                  )
        response_object = {
            'status': 'success',
            'message': 'Kiosk Qr Successfully generated.',
            'file_path': os.path.join(basedir, 'kioskqr{0}.svg'.format(kiosk_id)),
            'html_image': html_img
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        print(e)
        return response_object, 401


def get_kiosk_qr(kiosk_id):
    return send_file(os.path.join(basedir, 'kioskqr{0}.svg'.format(kiosk_id)), as_attachment=True,
                     attachment_filename="kioskqr{0}.svg".format(kiosk_id), mimetype='image/svg+xml')


def assign_kiosk(kiosk_id, data):
    kiosk = Kiosk.query.filter_by(id=kiosk_id).first()
    if not kiosk:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    elif kiosk.condition is "Non-functional":
        response_object = {
            'status': 'fail',
            'message': 'kiosk is non functional.'
        }
        return response_object, 409
    kiosk.condition = data['condition']
    kiosk.mf_id = data['mf_id']
    db.session.commit()
    return update_kiosk(kiosk)


def deassign_kiosk(kiosk_id, data):
    kiosk = Kiosk.query.filter_by(id=kiosk_id).first()
    if not kiosk:
        response_object = {
            'status': 'fail',
            'message': 'mf not found.'
        }
        return response_object, 404
    kiosk.condition = data['condition']
    kiosk.mf_id = data['mf_id']

    db.session.commit()
    return update_kiosk(kiosk)


def delete_a_kiosk(kiosk_id):
    kiosk = get_a_kiosk(kiosk_id)
    db.session.delete(kiosk)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Kiosk Successfully deleted.'
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

