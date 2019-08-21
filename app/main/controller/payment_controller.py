from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.payment_service import *
api = PaymentModeDto.api
_payment = PaymentModeDto.payment_mode


@api.route('/all')
class PaymentModeList(Resource):
    @api.doc('list_of_registered_payment_modes')
    @admin_token_required
    @api.marshal_list_with(_payment, envelope='data')
    def get(self):
        """List all registered payment modes"""
        return get_all_payment_modes()


@api.route('/new')
class PaymentModeList(Resource):
    @api.expect(_payment, validate=True)
    @api.response(201, 'payment mode successfully created.')
    @api.doc('create a new payment')
    @token_required
    def post(self):
        """Creates a new payment mode"""
        data = request.json
        return save_new_payment_mode(data=data)


@api.route('/<payment_mode_id>')
@api.param('payment_mode_id', 'The payment_mode identifier')
@api.response(404, 'payment_mode not found.')
class PaymentMode(Resource):
    @api.doc('get a payment_mode')
    @token_required
    @api.marshal_with(_payment)
    def get(self, payment_mode_id):
        """get a payment_mode given its identifier"""
        le_payment_mode = get_a_payment_mode(payment_mode_id)
        if not le_payment_mode:
            return {'success': False, 'message': 'payment_mode not found'}
        else:
            return le_payment_mode


@api.route('/<payment_mode_id>/edit')
@api.param('payment_mode_id', 'The payment_mode identifier')
@api.response(404, 'payment_mode not found.')
class PaymentMode(Resource):
    @api.expect(_payment, validate=False)
    @api.response(201, 'payment_mode successfully edited.')
    @api.doc('edit a new payment_mode')
    @token_required
    def put(self, payment_mode_id):
        """Edits a new payment_mode """
        le_payment_mode = get_a_payment_mode(payment_mode_id)
        if not le_payment_mode:
            return {'success': False, 'message': 'payment_mode not found'}
        data = request.json
        return edit_payment_mode(payment_mode_id, data=data)


@api.route('/<payment_mode_id>/delete')
@api.param('payment_mode_id', 'The payment_mode identifier')
@api.response(404, 'payment_mode not found.')
class Payment(Resource):
    @api.doc('delete an payment_mode')
    @token_required
    def delete(self, payment_mode_id):
        """ Delete payment_mode by id """
        le_payment_mode = get_a_payment_mode(payment_mode_id)
        if not le_payment_mode:
            return {'success': False, 'msg': 'payment_mode does not exist'}
        else:
            delete_a_payment_mode(payment_mode_id)
            return {'success': True, 'message': 'payment_mode deleted successfully'}
