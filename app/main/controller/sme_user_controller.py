from flask import request
from flask_restplus import Resource

from app.main.util.sme_decorator import *
from app.main.util.decorator import *
from ..util.dto import SmeUserDto
from ..service.sme_user_service import *

api = SmeUserDto.api
_sme_user = SmeUserDto.sme_user


@api.route('/')
class SmeUserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_sme_user, envelope='data')
    def get(self):
        """List all registered sme users"""
        return get_all_sme_users()

    @api.expect(_sme_user, validate=True)
    @api.response(201, 'Sme User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_sme_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
class SmeUser(Resource):
    @api.doc('get a sme')
    @admin_token_required
    @api.marshal_with(_sme_user)
    def get(self, id):
        """get a sme user given its identifier"""
        n_id = id if id.isdigit() else 0
        user = get_a_sme_user(n_id)
        if not user:
            return {'success': False, 'message': 'user not found'}
        else:
            return user


@api.route('/<id>/delete')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class SmeUser(Resource):
    @api.doc('delete a user')
    @admin_token_required
    def delete(self, id):
        """ Delete user by id """
        user = get_a_sme_user(int(id))
        if user is not None:
            delete_a_sme_user(user)
            return {'success': True}
        else:
            return {'success': False, 'msg': 'user does not exist'}
