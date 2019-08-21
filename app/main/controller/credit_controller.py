from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.credit_service import *
api = CreditDto.api
_credit = CreditDto.credit


@api.route('/all')
class CreditList(Resource):
    @api.doc('list_of_registered_penalties')
    @admin_token_required
    @api.marshal_list_with(_credit, envelope='data')
    def get(self):
        """List all registered penalties"""
        return get_all_credits()


@api.route('/new')
class CreditList(Resource):
    @api.expect(_credit, validate=True)
    @api.response(201, 'credit successfully created.')
    @api.doc('create a new credit')
    @token_required
    def post(self):
        """Creates a new credit"""
        data = request.json
        return save_new_credit(data=data)


@api.route('/<credit_id>')
@api.param('credit_id', 'The credit identifier')
@api.response(404, 'credit not found.')
class Credit(Resource):
    @api.doc('get a credit')
    @token_required
    @api.marshal_with(_credit)
    def get(self, credit_id):
        """get a credit given its identifier"""
        le_credit = get_an_credit(credit_id)
        if not le_credit:
            return {'success': False, 'message': 'credit not found'}
        else:
            return le_credit


@api.route('/<credit_id>/edit')
@api.param('credit_id', 'The credit identifier')
@api.response(404, 'credit not found.')
class Credit(Resource):
    @api.expect(_credit, validate=False)
    @api.response(201, 'credit successfully edited.')
    @api.doc('edit a new credit')
    @token_required
    def put(self, credit_id):
        """Edits a new credit """
        le_credit = get_an_credit(credit_id)
        if not le_credit:
            return {'success': False, 'message': 'credit not found'}
        data = request.json
        return edit_credit(credit_id, data=data)


@api.route('/<credit_id>/delete')
@api.param('credit_id', 'The credit identifier')
@api.response(404, 'credit not found.')
class Credit(Resource):
    @api.doc('delete an credit')
    @token_required
    def delete(self, credit_id):
        """ Delete credit by id """
        le_credit = get_an_credit(credit_id)
        if not le_credit:
            return {'success': False, 'msg': 'credit does not exist'}
        else:
            delete_an_credit(credit_id)
            return {'success': True, 'message': 'credit deleted successfully'}
