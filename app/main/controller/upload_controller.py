from flask_restplus import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os
from ..util.dto import *
from flask import url_for, send_from_directory
from ..service.upload_service import *

api = UploadDto.api

parser = reqparse.RequestParser()
parser.add_argument('file', type=FileStorage, location='files')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=False)
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'media')


@api.route('/upload')
@api.expect(upload_parser)
class Upload(Resource):
    decorators = []

    @api.doc('upload')
    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                'data': '',
                'message': 'No file found',
                'status': 'error'
            }
        photo = data['file']

        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(UPLOAD_FOLDER, filename))
            payload = {
                'filename': filename,
                'url': url_for('api.upload_uploaded_file', filename=filename),
                'title': filename
            }
            save_new_upload(payload)
            return {
                'data': '',
                'message': 'photo uploaded',
                'status': 'success',
                'url': url_for('api.upload_uploaded_file', filename=filename)
            }
        return {
            'data': '',
            'message': 'Something when wrong',
            'status': 'error'
        }


@api.route('/uploads/<filename>')
class UploadedFile(Resource):
    def get(self, filename):
        return send_from_directory(UPLOAD_FOLDER, filename)
