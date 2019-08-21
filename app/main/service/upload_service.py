from app.main import db
from app.main.model.upload import Upload


def save_new_upload(data):
    upload = Upload.query.filter_by(filename=data['filename']).first()
    if not upload:
        new_upload = Upload(
            filename=data['filename'],
            url=data['url'],
            title=data['filename']
        )
        save_changes(new_upload)
        return generate_new_upload(new_upload)
    else:
        response_object = {
            'status': 'fail',
            'message': 'upload already exists. Use existing resource'
        }
        return response_object, 409


def generate_new_upload(upload):
    try:
        response_object = {
            'status': 'success',
            'message': 'upload saved',
            'url': upload.url
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
