from flask_restplus import Resource
from app.main.util.decorator import token_required
from ..util.dto import *
from ..service.user_answer_service import *
api = UserAnswerDto.api
_user_answer = UserAnswerDto.user_answer


@api.route('/all')
class UserAnswerList(Resource):
    @api.doc('list_of_registered_answers')
    @token_required
    @api.marshal_list_with(_user_answer, envelope='data')
    def get(self):
        """List all registered user_answers"""
        return get_all_user_answers()


@api.route('/daily_count/<town_id>')
class UserAnswerList(Resource):
    @api.doc('count')
    def get(self, town_id):
        """Count"""
        return get_user_answer_count(town_id)


@api.route('/monthly_count/<town_id>')
class UserAnswerList(Resource):
    @api.doc('monthly_count')
    def get(self, town_id):
        """Monthly count"""
        return get_monthly_count(town_id)


@api.route('/new')
class UserAnswerList(Resource):
    @api.expect(_user_answer, validate=True)
    @api.response(201, 'user_answer successfully created.')
    @api.doc('create a new user_answer')
    @token_required
    def post(self):
        """Creates a new user_answer """
        data = request.json
        return save_new_user_answer(data=data)


@api.route('/<user_answer_id>')
@api.param('user_answer_id', 'The user_answer identifier')
@api.response(404, 'user_answer not found.')
class UserAnswer(Resource):
    @api.doc('get a user_answer')
    @token_required
    @api.marshal_with(_user_answer)
    def get(self, user_answer_id):
        """get a user_answer given its identifier"""
        le_user_answer = get_a_user_answer(user_answer_id)
        if not le_user_answer:
            return {'success': False, 'message': 'user_answer not found'}
        else:
            return le_user_answer


@api.route('/<user_answer_id>/edit')
@api.param('user_answer_id', 'The user_answer identifier')
@api.response(404, 'user_answer not found.')
class UserAnswer(Resource):
    @api.expect(_user_answer, validate=False)
    @api.response(201, 'user_answer successfully edited.')
    @api.doc('edit a new user_answer')
    @token_required
    def put(self, user_answer_id):
        """Edits a user_answer"""
        le_user_answer = get_a_user_answer(user_answer_id)
        if not le_user_answer:
            return {'success': False, 'message': 'user_answer not found'}
        data = request.json
        return edit_user_answer(user_answer_id, data=data)


@api.route('/<user_answer_id>/delete')
@api.param('user_answer_id', 'The user_answer identifier')
@api.response(404, 'user_answer not found.')
class UserAnswer(Resource):
    @api.doc('delete an user_answer')
    @token_required
    def delete(self, user_answer_id):
        """ Delete user_answer by id """
        le_user_answer = get_a_user_answer(user_answer_id)
        if not le_user_answer:
            return {'success': False, 'msg': 'user_answer does not exist'}
        else:
            return delete_a_user_answer(user_answer_id)
