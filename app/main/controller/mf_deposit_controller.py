from flask import request
from flask_restplus import Resource
from app.main.util.officer_decorator import *
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.mf_deposit_service import *
api = MfDepositDto.api
_mf_deposit = MfDepositDto.mf_deposit


@api.route('/all')
class MfDepositList(Resource):
    @api.doc('list_of_registered_mf_deposits')
    @api.marshal_list_with(_mf_deposit, envelope='data')
    def get(self):
        """List all registered mf deposits"""
        return get_all_mf_deposits()


@api.route('/<mf_id>/all')
class MfDepositList(Resource):
    @api.doc('list_of_registered_mf_deposits')
    @api.marshal_list_with(_mf_deposit, envelope='data')
    def get(self, mf_id):
        """List all registered mf deposits"""
        return get_all_mf_deposits_by_mf(mf_id)


@api.route('/new')
class MfDepositList(Resource):
    @api.expect(_mf_deposit, validate=True)
    @api.response(201, 'deposit successfully created.')
    @api.doc('create a new deposit')
    @admin_token_required
    def post(self):
        """Creates a new mf deposit """
        data = request.json
        return save_new_mf_deposit(data=data)


@api.route('/<mf_deposit_id>')
@api.param('mf_deposit_id', 'The deposit identifier')
@api.response(404, 'mf_deposit not found.')
class MfDeposit(Resource):
    @api.doc('get a mf_deposit')
    @api.marshal_with(_mf_deposit)
    def get(self, mf_deposit_id):
        """get a mf deposit given its identifier"""
        le_mf_deposit = get_an_mf_deposit(mf_deposit_id)
        if not le_mf_deposit:
            return {'success': False, 'message': 'mf_deposit not found'}
        else:
            return le_mf_deposit


@api.route('/<mf_deposit_id>/edit')
@api.param('mf_deposit_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfDeposit(Resource):
    @api.expect(_mf_deposit, validate=False)
    @api.response(201, 'mf successfully edited.')
    @api.doc('edit a new mf')
    @admin_token_required
    def put(self, mf_deposit_id):
        """Edits a mf deposit"""
        le_mf_deposit = get_an_mf_deposit(mf_deposit_id)
        if not le_mf_deposit:
            return {'success': False, 'message': 'mf not found'}
        data = request.json
        return edit_mf_deposit(mf_deposit_id, data=data)


@api.route('/<mf_deposit_id>/delete')
@api.param('mf_deposit_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfDeposit(Resource):
    @api.doc('delete an mf')
    @admin_token_required
    def delete(self, mf_deposit_id):
        """ Delete mf deposit by id """
        le_mf_deposit = get_an_mf_deposit(mf_deposit_id)
        if not le_mf_deposit:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            delete_an_mf_deposit(mf_deposit_id)
            return {'success': True, 'message': 'mf deleted successfully'}


@api.route('/mf/<mf_id>')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfDepositById(Resource):
    @api.doc('find an mf deposit')
    @api.marshal_list_with(_mf_deposit, envelope='data')
    def get(self, mf_id):
        """ find an mf deposit by mf id """
        return get_mf_deposit_by_mf_id(mf_id)
