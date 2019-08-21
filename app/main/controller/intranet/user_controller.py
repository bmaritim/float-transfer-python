from flask import request
from flask_restplus import Resource

from app.main.util.intranet_decorator import *
from app.main.util.decorator import *
from ...util.dto import IUserDto
from ...service.intranet.user_service import *

api = IUserDto.api
_i_user = IUserDto.i_user


@api.route('/')
class IUserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_i_user, envelope='data')
    def get(self):
        """List all registered i users"""
        return get_all_i_users()

    @api.expect(_i_user, validate=True)
    @api.response(201, 'i User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_i_user(data=data)


@api.route('/<i_user_id>')
@api.param('i_user_id', 'The User identifier')
class IUser(Resource):
    @api.doc('get a i')
    @admin_token_required
    @api.marshal_with(_i_user)
    def get(self, i_user_id):
        """get a i user given its identifier"""
        le_i_user = get_a_i_user(i_user_id)
        if not user:
            return {'success': False, 'message': 'user not found'}
        else:
            return le_i_user


@api.route('/<i_user_id>/edit')
@api.param('i_user_id', 'The User identifier')
class IUser(Resource):
    @api.doc('edit')
    @admin_token_required
    def put(self, i_user_id):
        """Edits a user"""
        le_i_user = get_a_i_user(i_user_id)
        if not le_i_user:
            return {'success': False, 'message': 'user not found'}
        data = request.json
        return edit_an_i_user(i_user_id, data=data)


@api.route('/<i_user_id>/delete')
@api.param('i_user_id', 'The User identifier')
@api.response(404, 'User not found.')
class IUser(Resource):
    @api.doc('delete a user')
    @admin_token_required
    def delete(self, i_user_id):
        """ Delete user by id """
        le_user = get_a_i_user(i_user_id)
        if not le_user:
            return {'success': False, 'msg': 'user does not exist'}
        else:
            return delete_a_i_user(i_user_id)
