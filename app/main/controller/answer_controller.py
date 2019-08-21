from flask import request
from flask_restplus import Resource
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.answer_service import *
api = AnswerDto.api
_answer = AnswerDto.answer


@api.route('/all')
class AnswerList(Resource):
    @api.doc('list_of_registered_answers')
    @token_required
    @api.marshal_list_with(_answer, envelope='data')
    def get(self):
        """List all registered answers"""
        return get_all_answers()


@api.route('/new')
class AnswerList(Resource):
    @api.expect(_answer, validate=True)
    @api.response(201, 'answer successfully created.')
    @api.doc('create a new answer')
    @token_required
    def post(self):
        """Creates a new answer """
        data = request.json
        return save_new_answer(data=data)


@api.route('/<answer_id>')
@api.param('answer_id', 'The answer identifier')
@api.response(404, 'answer not found.')
class Answer(Resource):
    @api.doc('get a answer')
    @token_required
    @api.marshal_with(_answer)
    def get(self, answer_id):
        """get a answer given its identifier"""
        le_answer = get_an_answer(answer_id)
        if not le_answer:
            return {'success': False, 'message': 'answer not found'}
        else:
            return le_answer


@api.route('/<answer_id>/edit')
@api.param('answer_id', 'The answer identifier')
@api.response(404, 'answer not found.')
class Answer(Resource):
    @api.expect(_answer, validate=False)
    @api.response(201, 'answer successfully edited.')
    @api.doc('edit a new answer')
    @token_required
    def put(self, answer_id):
        """Edits a answer"""
        le_answer = get_an_answer(answer_id)
        if not le_answer:
            return {'success': False, 'message': 'answer not found'}
        data = request.json
        return edit_answer(answer_id, data=data)


@api.route('/<answer_id>/delete')
@api.param('answer_id', 'The answer identifier')
@api.response(404, 'answer not found.')
class Answer(Resource):
    @api.doc('delete an answer')
    @token_required
    def delete(self, answer_id):
        """ Delete answer by id """
        le_answer = get_an_answer(answer_id)
        if not le_answer:
            return {'success': False, 'msg': 'answer does not exist'}
        else:
            return delete_a_answer(answer_id)



