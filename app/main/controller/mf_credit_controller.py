from flask import request
from flask_restplus import Resource
from app.main.util.officer_decorator import *
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.mf_credit_service import *
api = MfCreditDto.api
_mf_credit = MfCreditDto.mf_credit


@api.route('/all')
class MfCreditList(Resource):
    @api.doc('list_of_registered_mf_credits')
    @api.marshal_list_with(_mf_credit, envelope='data')
    def get(self):
        """List all registered mf credits"""
        return get_all_mf_credits()


@api.route('/<mf_id>/all')
class MfCreditList(Resource):
    @api.doc('list_of_registered_mf_credits')
    @api.marshal_list_with(_mf_credit, envelope='data')
    def get(self, mf_id):
        """List all registered mf credits"""
        return get_all_mf_credits_by_mf(mf_id)


@api.route('/new')
class MfCreditList(Resource):
    @api.expect(_mf_credit, validate=True)
    @api.response(201, 'credit successfully created.')
    @api.doc('create a new credit')
    @admin_token_required
    def post(self):
        """Creates a new mf credit """
        data = request.json
        return save_new_mf_credit(data=data)


@api.route('/<mf_credit_id>')
@api.param('mf_credit_id', 'The credit identifier')
@api.response(404, 'mf_credit not found.')
class MfCredit(Resource):
    @api.doc('get a mf_credit')
    @api.marshal_with(_mf_credit)
    def get(self, mf_credit_id):
        """get a mf credit given its identifier"""
        le_mf_credit = get_an_mf_credit(mf_credit_id)
        if not le_mf_credit:
            return {'success': False, 'message': 'mf_credit not found'}
        else:
            return le_mf_credit


@api.route('/<mf_credit_id>/edit')
@api.param('mf_credit_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfCredit(Resource):
    @api.expect(_mf_credit, validate=False)
    @api.response(201, 'mf successfully edited.')
    @api.doc('edit a new mf')
    @admin_token_required
    def put(self, mf_credit_id):
        """Edits a mf credit"""
        le_mf_credit = get_an_mf_credit(mf_credit_id)
        if not le_mf_credit:
            return {'success': False, 'message': 'mf not found'}
        data = request.json
        return edit_mf_credit(mf_credit_id, data=data)


@api.route('/<mf_credit_id>/delete')
@api.param('mf_credit_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfCredit(Resource):
    @api.doc('delete an mf')
    @admin_token_required
    def delete(self, mf_credit_id):
        """ Delete mf credit by id """
        le_mf_credit = get_an_mf_credit(mf_credit_id)
        if not le_mf_credit:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            delete_an_mf_credit(mf_credit_id)
            return {'success': True, 'message': 'mf deleted successfully'}
