from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ...util.dto import *
from ...service.intranet.upload_service import *
api = IUploadDto.api
_upload = IUploadDto.i_upload


@api.route('/all')
class UploadList(Resource):
    @api.doc('list_of_uploads')
    @admin_token_required
    @api.marshal_list_with(_upload, envelope='data')
    def get(self):
        """List all registered uploads"""
        return get_all_uploads()


@api.route('/new')
class UploadList(Resource):
    @api.expect(_upload, validate=True)
    @api.response(201, 'upload successfully created.')
    @api.doc('create a new upload')
    @token_required
    def post(self):
        """Creates a new upload"""
        data = request.json
        return save_new_upload(data=data)


@api.route('/<upload_id>')
@api.param('upload_id', 'The upload identifier')
@api.response(404, 'upload not found.')
class Upload(Resource):
    @api.doc('get a upload')
    @token_required
    @api.marshal_with(_upload)
    def get(self, upload_id):
        """get a upload given its identifier"""
        le_upload = get_a_upload(upload_id)
        if not le_upload:
            return {'success': False, 'message': 'upload not found'}
        else:
            return le_upload


@api.route('/<upload_id>/edit')
@api.param('upload_id', 'The upload identifier')
@api.response(404, 'upload not found.')
class Upload(Resource):
    @api.expect(_upload, validate=False)
    @api.response(201, 'upload successfully edited.')
    @api.doc('edit a new upload')
    @token_required
    def put(self, upload_id):
        """Edits a new upload """
        le_upload = get_a_upload(upload_id)
        if not le_upload:
            return {'success': False, 'message': 'upload not found'}
        data = request.json
        return edit_upload(upload_id, data=data)


@api.route('/<upload_id>/delete')
@api.param('upload_id', 'The upload identifier')
@api.response(404, 'upload not found.')
class Upload(Resource):
    @api.doc('delete an upload')
    @token_required
    def delete(self, upload_id):
        """ Delete upload by id """
        le_upload = get_a_upload(upload_id)
        if not le_upload:
            return {'success': False, 'msg': 'upload does not exist'}
        else:
            return delete_a_upload(upload_id)
