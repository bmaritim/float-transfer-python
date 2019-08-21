from flask import request
from flask_restplus import Resource
from app.main.util.officer_decorator import *
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.mf_service import *
api = MfDto.api
_mf = MfDto.mf


@api.route('/all')
class MfList(Resource):
    @api.doc('list_of_registered_mfs')
    @token_required
    @api.marshal_list_with(_mf, envelope='data')
    def get(self):
        """List all registered mf"""
        return get_all_mfs()


@api.route('/new')
class MfList(Resource):
    @api.expect(_mf, validate=True)
    @api.response(201, 'mf successfully created.')
    @api.doc('create a new mf')
    @token_required
    def post(self):
        """Creates a new mf """
        data = request.json
        return save_new_mf(data=data)


@api.route('/<mf_id>')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class Mf(Resource):
    @api.doc('get a mf')
    @token_required
    @api.marshal_with(_mf)
    def get(self, mf_id):
        """get a mf given its identifier"""
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'message': 'mf not found'}
        else:
            return le_mf


@api.route('/<mf_id>/edit')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class Mf(Resource):
    @api.expect(_mf, validate=False)
    @api.response(201, 'mf successfully edited.')
    @api.doc('edit a new mf')
    @token_required
    def put(self, mf_id):
        """Edits a new mf """
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'message': 'mf not found'}
        data = request.json
        return edit_mf(mf_id, data=data)


@api.route('/<mf_id>/delete')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class Mf(Resource):
    @api.doc('delete an mf')
    @token_required
    def delete(self, mf_id):
        """ Delete mf by id """
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            delete_an_mf(mf_id)
            return {'success': True, 'message': 'mf deleted successfully'}


@api.route('/<mf_id>/deploy')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfDeploy(Resource):
    @api.doc('deploy an mf')
    @token_required
    def post(self, mf_id):
        """deploy an mf given its identifier"""
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            data = request.json
            return deploy_an_mf(mf_id, data=data)


@api.route('/<mf_id>/suspend')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfSuspend(Resource):
    @api.doc('suspend an mf')
    @token_required
    def post(self, mf_id):
        """suspend an mf given its identifier"""
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            suspended_mf = suspend_an_mf(mf_id)
            return suspended_mf


@api.route('/<mf_id>/terminate')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfTerminate(Resource):
    @api.doc('terminate an mf')
    @token_required
    def post(self, mf_id):
        """terminate an mf given its identifier"""
        le_mf = get_an_mf(mf_id)
        if not le_mf:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            terminated_mf = terminate_an_mf(mf_id)
            return terminated_mf


@api.route('/<mf_id>/get_deposit_amount')
@api.param('mf_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfGetDeposit(Resource):
    @api.doc('get an mf depo')
    def get(self, mf_id):
        """mf deposits amount"""
        return get_an_mf_deposit(mf_id)
