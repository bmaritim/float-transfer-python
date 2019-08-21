from flask import request
from flask_restplus import Resource, reqparse
from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.officer_service import *
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

api = OfficerDto.api
_officer = OfficerDto.officer

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
            return {
                'data': '',
                'message': 'photo uploaded',
                'status': 'success'
            }
        return {
            'data': '',
            'message': 'Something when wrong',
            'status': 'error'
        }


@api.route('/all')
class OfficerList(Resource):
    @api.doc('list_of_registered_officers')
    @admin_token_required
    @api.marshal_list_with(_officer, envelope='data')
    def get(self):
        """List all registered officer"""
        return get_all_officers()


@api.route('/new')
class OfficerList(Resource):
    @api.expect(_officer, validate=True)
    @api.response(201, 'officer successfully created.')
    @api.doc('create a new officer')
    @token_required
    def post(self):
        """Creates a new officer """
        data = request.json
        return save_new_officer(data=data)


@api.route('/<officer_id>')
@api.param('officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class Officer(Resource):
    @api.doc('get a officer')
    @token_required
    @api.marshal_with(_officer)
    def get(self, officer_id):
        """get a officer given its identifier"""
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'message': 'officer not found'}
        else:
            return le_officer


@api.route('/<officer_id>/edit')
@api.param('officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class Officer(Resource):
    @api.expect(_officer, validate=False)
    @api.response(201, 'officer successfully edited.')
    @api.doc('edit a new officer')
    @token_required
    def put(self, officer_id):
        """Edits a new officer """
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'message': 'officer not found'}
        data = request.json
        return edit_officer(officer_id, data=data)


@api.route('/<officer_id>/delete')
@api.param('officer_id', 'The Officer identifier')
@api.response(404, 'Officer not found.')
class Officer(Resource):
    @api.doc('delete an officer')
    @token_required
    def delete(self, officer_id):
        """ Delete officer by id """
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'msg': 'officer does not exist'}
        else:
            return delete_an_officer(officer_id)


@api.route('/<officer_id>/deploy')
@api.param('officer_id', 'The officer identifier')
@api.param('deployed_town_id', 'town deployed to')
@api.param('deployed_district_id', 'district deployed to')
@api.param('deployed_country_id', 'country deployed to')
@api.response(404, 'officer not found.')
class OfficerDeploy(Resource):
    @api.doc('deploy an officer')
    @token_required
    def post(self, officer_id):
        """deploy an officer given its identifier"""
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'msg': 'officer does not exist'}
        else:
            data = request.json
            return deploy_an_officer(officer_id, data=data)


@api.route('/<officer_id>/suspend')
@api.param('officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class OfficerSuspend(Resource):
    @api.doc('suspend an officer')
    @token_required
    def post(self, officer_id):
        """suspend an officer given its identifier"""
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'msg': 'officer does not exist'}
        else:
            suspended_officer = suspend_an_officer(officer_id)
            return suspended_officer


@api.route('/<officer_id>/terminate')
@api.param('officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class OfficerTerminate(Resource):
    @api.doc('terminate an officer')
    @token_required
    def post(self, officer_id):
        """terminate an officer given its identifier"""
        le_officer = get_an_officer(officer_id)
        if not le_officer:
            return {'success': False, 'msg': 'officer does not exist'}
        else:
            terminated_officer = terminate_an_officer(officer_id)
            return terminated_officer


