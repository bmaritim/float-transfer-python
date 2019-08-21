from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.leasing_service import *
api = LeasingDto.api
_leasing = LeasingDto.leasing


@api.route('/all')
class PaymentModeList(Resource):
    @api.doc('list_of_registered_leasing')
    @admin_token_required
    @api.marshal_list_with(_leasing, envelope='data')
    def get(self):
        """List all registered payment modes"""
        return get_all_leasing_fees()


@api.route('/new')
class PaymentModeList(Resource):
    @api.expect(_leasing, validate=True)
    @api.response(201, 'payment mode successfully created.')
    @api.doc('create a new payment')
    @token_required
    def post(self):
        """Creates a new payment mode"""
        data = request.json
        return save_new_leasing_fee(data=data)


@api.route('/<leasing_id>')
@api.param('leasing_id', 'The leasing_fee identifier')
@api.response(404, 'leasing_fee not found.')
class PaymentMode(Resource):
    @api.doc('get a leasing_fee')
    @token_required
    @api.marshal_with(_leasing)
    def get(self, leasing_id):
        """get a leasing_fee given its identifier"""
        le_leasing = get_a_leasing_fee(leasing_id)
        if not le_leasing:
            return {'success': False, 'message': 'leasing_fee not found'}
        else:
            return le_leasing


@api.route('/<leasing_id>/edit')
@api.param('leasing_id', 'The leasing_fee identifier')
@api.response(404, 'leasing_fee not found.')
class PaymentMode(Resource):
    @api.expect(_leasing, validate=False)
    @api.response(201, 'leasing_fee successfully edited.')
    @api.doc('edit a new leasing_fee')
    @token_required
    def put(self, leasing_id):
        """Edits a new leasing_fee """
        le_leasing = get_a_leasing_fee(leasing_id)
        if not le_leasing:
            return {'success': False, 'message': 'leasing_fee not found'}
        data = request.json
        return edit_leasing_fee(leasing_id, data=data)


@api.route('/<leasing_id>/delete')
@api.param('leasing_id', 'The leasing_fee identifier')
@api.response(404, 'leasing_fee not found.')
class Payment(Resource):
    @api.doc('delete a leasing_fee')
    @token_required
    def delete(self, leasing_id):
        """ Delete leasing_fee by id """
        le_leasing = get_a_leasing_fee(leasing_id)
        if not le_leasing:
            return {'success': False, 'msg': 'leasing_fee does not exist'}
        else:
            delete_a_leasing_fee(leasing_id)
            return {'success': True, 'message': 'leasing_fee deleted successfully'}
