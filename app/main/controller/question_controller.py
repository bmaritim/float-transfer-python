from flask import request
from flask_restplus import Resource
from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from ..util.dto import *
from ..service.question_service import *
api = QuestionDto.api
_question = QuestionDto.question


@api.route('/all')
class QuestionList(Resource):
    @api.doc('list_of_registered_questions')
    @api.marshal_list_with(_question, envelope='data')
    def get(self):
        """List all registered questions"""
        return get_all_questions()


@api.route('/new')
class QuestionList(Resource):
    @api.expect(_question, validate=True)
    @api.response(201, 'question successfully created.')
    @api.doc('create a new question')
    def post(self):
        """Creates a new question """
        data = request.json
        return save_new_question(data=data)


@api.route('/<question_id>')
@api.param('question_id', 'The question identifier')
@api.response(404, 'question not found.')
class Question(Resource):
    @api.doc('get a question')
    @api.marshal_with(_question)
    def get(self, question_id):
        """get a question given its identifier"""
        le_question = get_a_question(question_id)
        if not le_question:
            return {'success': False, 'message': 'question not found'}
        else:
            return le_question


@api.route('/<question_id>/edit')
@api.param('question_id', 'The question identifier')
@api.response(404, 'question not found.')
class Question(Resource):
    @api.expect(_question, validate=False)
    @api.response(201, 'question successfully edited.')
    @api.doc('edit a new question')
    def put(self, question_id):
        """Edits a question"""
        le_question = get_a_question(question_id)
        if not le_question:
            return {'success': False, 'message': 'question not found'}
        data = request.json
        return edit_question(question_id, data=data)


@api.route('/<question_id>/delete')
@api.param('question_id', 'The question identifier')
@api.response(404, 'question not found.')
class Question(Resource):
    @api.doc('delete an question')
    def delete(self, question_id):
        """ Delete question by id """
        le_question = get_a_question(question_id)
        if not le_question:
            return {'success': False, 'msg': 'question does not exist'}
        else:
            return delete_a_question(question_id)



