from flask import request
from flask_restplus import Resource

from app.main.util.sme_decorator import *
from app.main.util.decorator import *
from ..util.dto import SmeDto
from ..service.sme_service import *
from ..service.sme_user_service import *

api = SmeDto.api
_sme = SmeDto.sme


@api.route('/')
class SmeList(Resource):
    @api.doc('list_of_registered_smes')
    @sme_admin_token_required
    @api.marshal_list_with(_sme, envelope='data')
    def get(self):
        """List all registered smes"""
        return get_all_smes()

    @api.expect(_sme, validate=True)
    @api.response(201, 'Sme successfully created.')
    @sme_admin_token_required
    @api.doc('create a new sme')
    def post(self):
        """Creates a new sme """
        data = request.json
        return save_new_sme(data=data)


@api.route('/<id>')
@api.param('id', 'The sme identifier')
class Sme(Resource):
    @api.doc('get a sme')
    @sme_admin_token_required
    @api.marshal_with(_sme)
    def get(self, id):
        """get a sme given its identifier"""
        n_id = id if id.isdigit() else 0
        sme = get_a_sme(n_id)
        if not sme:
            return {'success': False, 'message': 'sme not found'}
        else:
            return sme


@api.route('/<id>/delete')
@api.param('id', 'The sme identifier')
@api.response(404, 'sme not found.')
class Sme(Resource):
    @api.doc('delete a sme')
    @sme_admin_token_required
    def delete(self, id):
        """ Delete sme by id """
        sme = get_a_sme(int(id))
        if sme is not None:
            delete_a_sme(sme)
            return {'success': True}
        else:
            return {'success': False, 'msg': 'sme user does not exist'}
