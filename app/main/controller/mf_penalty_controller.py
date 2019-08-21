from flask import request
from flask_restplus import Resource
from app.main.util.officer_decorator import *
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.mf_penalty_service import *
api = MfPenaltyDto.api
_mf_penalty = MfPenaltyDto.mf_penalty


@api.route('/all')
class MfPenaltyList(Resource):
    @api.doc('list_of_registered_mf_penalties')
    @api.marshal_list_with(_mf_penalty, envelope='data')
    def get(self):
        """List all registered mf penalties"""
        return get_all_mf_penalties()


@api.route('/<mf_id>/all')
class MfPenaltyList(Resource):
    @api.doc('list_of_registered_mf_penalties')
    @api.marshal_list_with(_mf_penalty, envelope='data')
    def get(self, mf_id):
        """List all registered mf penalties"""
        return get_all_mf_penalties_by_mf(mf_id)


@api.route('/new')
class MfPenaltyList(Resource):
    @api.expect(_mf_penalty, validate=True)
    @api.response(201, 'mf successfully created.')
    @api.doc('create a new mf')
    @admin_token_required
    def post(self):
        """Creates a new mf penalty"""
        data = request.json
        return save_new_mf_penalty(data=data)


@api.route('/<mf_penalty_id>')
@api.param('mf_penalty_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfPenalty(Resource):
    @api.doc('get a mf')
    @api.marshal_with(_mf_penalty)
    def get(self, mf_penalty_id):
        """get a mf penalty given its identifier"""
        le_mf_penalty = get_an_mf_penalty(mf_penalty_id)
        if not le_mf_penalty:
            return {'success': False, 'message': 'mf penalty not found'}
        else:
            return le_mf_penalty


@api.route('/<mf_penalty_id>/edit')
@api.param('mf_penalty_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfPenalty(Resource):
    @api.expect(_mf_penalty, validate=False)
    @api.response(201, 'mf successfully edited.')
    @api.doc('edit a new mf')
    @admin_token_required
    def put(self, mf_penalty_id):
        """Edits a new mf """
        le_mf_penalty = get_an_mf_penalty(mf_penalty_id)
        if not le_mf_penalty:
            return {'success': False, 'message': 'mf penalty not found'}
        data = request.json
        return edit_mf_penalty(mf_penalty_id, data=data)


@api.route('/<mf_penalty_id>/delete')
@api.param('mf_penalty_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfPenalty(Resource):
    @api.doc('delete an mf')
    @admin_token_required
    def delete(self, mf_penalty_id):
        """ Delete mf penalty by id """
        le_mf_penalty = get_an_mf_penalty(mf_penalty_id)
        if not le_mf_penalty:
            return {'success': False, 'msg': 'mf penalty does not exist'}
        else:
            return delete_an_mf_penalty(mf_penalty_id)
