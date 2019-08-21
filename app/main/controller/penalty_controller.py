from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.penalty_service import *
api = PenaltyDto.api
_penalty = PenaltyDto.penalty


@api.route('/all')
class PenaltyList(Resource):
    @api.doc('list_of_registered_penalties')
    @admin_token_required
    @api.marshal_list_with(_penalty, envelope='data')
    def get(self):
        """List all registered penalties"""
        return get_all_penalties()


@api.route('/new')
class PenaltyList(Resource):
    @api.expect(_penalty, validate=True)
    @api.response(201, 'penalty successfully created.')
    @api.doc('create a new penalty')
    @token_required
    def post(self):
        """Creates a new penalty"""
        data = request.json
        return save_new_penalty(data=data)


@api.route('/<penalty_id>')
@api.param('penalty_id', 'The penalty identifier')
@api.response(404, 'penalty not found.')
class Penalty(Resource):
    @api.doc('get a penalty')
    @token_required
    @api.marshal_with(_penalty)
    def get(self, penalty_id):
        """get a penalty given its identifier"""
        le_penalty = get_an_penalty(penalty_id)
        if not le_penalty:
            return {'success': False, 'message': 'penalty not found'}
        else:
            return le_penalty


@api.route('/<penalty_id>/edit')
@api.param('penalty_id', 'The penalty identifier')
@api.response(404, 'penalty not found.')
class Penalty(Resource):
    @api.expect(_penalty, validate=False)
    @api.response(201, 'penalty successfully edited.')
    @api.doc('edit a new penalty')
    @token_required
    def put(self, penalty_id):
        """Edits a new penalty """
        le_penalty = get_an_penalty(penalty_id)
        if not le_penalty:
            return {'success': False, 'message': 'penalty not found'}
        data = request.json
        return edit_penalty(penalty_id, data=data)


@api.route('/<penalty_id>/delete')
@api.param('penalty_id', 'The penalty identifier')
@api.response(404, 'penalty not found.')
class Penalty(Resource):
    @api.doc('delete an penalty')
    @token_required
    def delete(self, penalty_id):
        """ Delete penalty by id """
        le_penalty = get_an_penalty(penalty_id)
        if not le_penalty:
            return {'success': False, 'msg': 'penalty does not exist'}
        else:
            delete_an_penalty(penalty_id)
            return {'success': True, 'message': 'penalty deleted successfully'}
