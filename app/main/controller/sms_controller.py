from flask import request
from flask_restplus import Resource


from app.main.util.decorator import *
from ..util.dto import SmsDto
from ..service.sms_service import *

api = SmsDto.api
_sms = SmsDto.sms


@api.route('/')
class SmsList(Resource):
    @api.doc('list_of_registered_smss')
    @api.marshal_list_with(_sms, envelope='data')
    def get(self):
        """List all registered smss"""
        return get_all_smss()

    @api.expect(_sms, validate=True)
    @api.response(201, 'sms successfully created.')
    @api.doc('create a new sms')
    def post(self):
        """Creates a new sms """
        data = request.json
        return save_new_sms(data=data)


@api.route('/<sms_id>')
@api.param('sms_id', 'The sms identifier')
@api.response(404, 'sms not found.')
class Sms(Resource):
    @api.doc('get an sms')
    @api.marshal_with(_sms)
    def get(self, sms_id):
        """get an sms given its identifier"""
        sms = get_a_sms(sms_id)
        if not sms:
            api.abort(404)
        else:
            return sms


@api.route('/code/<generated_code>')
@api.param('generated_code', 'The sms identifier')
@api.response(404, 'sms not found.')
class Sms(Resource):
    @api.doc('get an sms')
    @token_required
    @api.marshal_with(_sms)
    def get(self, generated_code):
        """get an sms given its identifier"""
        sms = get_a_sms_by_code(generated_code)
        if not sms:
            api.abort(404)
        else:
            return sms


@api.route('/<int:sms_id>/delete')
@api.param('sms_id', 'The sms identifier')
@api.response(404, 'sms not found.')
class Sms(Resource):
    @api.doc('delete a sms')
    @admin_token_required
    def delete(self, sms_id):
        """ Delete sms by id """
        sms = get_a_sms(sms_id)
        if sms is not None:
            return delete_an_sms(sms)
        else:
            return {'success': False, 'msg': 'sms does not exist'}


@api.route('/confirm_token/<generated_code>')
@api.param('generated_code', 'The identifier')
@api.response(404, 'sms not found.')
class SmsConfirm(Resource):
    @api.response(201, 'sms successfully confirmed.')
    @api.doc('confirm token')
    def post(self, generated_code):
        """Edits a new payment_mode """
        le_sms = get_a_sms_by_code(generated_code)
        if not le_sms:
            return {'success': False, 'message': 'sms not found'}
        return check_token_code(generated_code)
