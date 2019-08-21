from flask import request
from flask_restplus import Resource

from app.main.util.decorator import *
from ..util.dto import *
from ..service.role_service import *
api = RoleDto.api
_role = RoleDto.role


@api.route('/all')
class RoleList(Resource):
    @api.doc('list_of_roles')
    @admin_token_required
    @api.marshal_list_with(_role, envelope='data')
    def get(self):
        """List all roles"""
        return get_all_roles()


@api.route('/new')
class RoleList(Resource):
    @api.expect(_role, validate=True)
    @api.response(201, 'role successfully created.')
    @api.doc('create a new role')
    @token_required
    @permission_access('create_role')
    def post(self):
        """Creates a new role """
        data = request.json
        return save_new_role(data=data)


@api.route('/<role_id>')
@api.param('role_id', 'The role identifier')
@api.response(404, 'role not found.')
class Role(Resource):
    @api.doc('get a role')
    @token_required
    @api.marshal_with(_role)
    def get(self, role_id):
        """get a role given its identifier"""
        role = get_a_role(role_id)
        if not role:
            return {'success': False, 'msg': 'role does not exist'}
        else:
            return role


@api.route('/<role_id>/edit_permissions')
@api.param('role_id', 'The role identifier')
@api.response(404, 'role not found.')
class Role(Resource):
    @api.doc('edit role permissions')
    @admin_token_required
    def put(self, role_id):
        """edit role permissions"""
        role = get_a_role(role_id)
        if not role:
            return {'success': False, 'msg': 'role does not exist'}
        else:
            data = request.json
            return edit_role_permissions(role_id=role_id, data=data)


