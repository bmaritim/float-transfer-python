from flask import request
from flask_restplus import Resource

from app.main.util.decorator import *
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @permission_access('read_user')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @admin_token_required
    @permission_access('create_user')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
class User(Resource):
    @api.doc('get a user')
    @admin_token_required
    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        n_id = id if id.isdigit() else 0
        user = get_a_user(n_id)
        if not user:
            return {'success': False, 'message': 'user not found'}
        else:
            return user


@api.route('/<id>/delete')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('delete a user')
    @admin_token_required
    def delete(self, id):
        """ Delete user by id """
        user = get_a_user(int(id))
        if user is not None:
            delete_a_user(user)
            return {'success': True}
        else:
            return {'success': False, 'msg': 'user does not exist'}
