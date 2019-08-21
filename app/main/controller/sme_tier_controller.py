from flask import request
from flask_restplus import Resource

from app.main.util.sme_decorator import *
from app.main.util.decorator import *
from ..util.dto import SmeTierDto
from ..service.sme_tier_service import *

api = SmeTierDto.api
_sme_tier = SmeTierDto.sme_tier


@api.route('/all')
class SmeTierList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @permission_access('read_user')
    @api.marshal_list_with(_sme_tier, envelope='data')
    def get(self):
        """List all registered sme tiers"""
        return get_all_sme_tiers()


@api.route('/create')
class SmeTierList(Resource):
    @api.expect(_sme_tier, validate=True)
    @api.response(201, 'Sme tier successfully created.')
    @admin_token_required
    @api.doc('create a new sme tier')
    def post(self):
        """Creates a new sme tier """
        data = request.json
        return save_new_sme_tier(data=data)

@api.route('/<id>')
@api.param('id', 'The sme tier identifier')
class SmeTier(Resource):
    @api.doc('get a sme')
    @admin_token_required
    @api.marshal_with(_sme_tier)
    def get(self, id):
        """get a sme tier given its identifier"""
        n_id = id if id.isdigit() else 0
        tier = get_a_sme_tier(n_id)
        if not tier:
            return {'success': False, 'message': 'tier not found'}
        else:
            return tier


@api.route('/<id>/delete')
@api.param('id', 'The sme tier identifier')
@api.response(404, 'Tier not found.')
class SmeTier(Resource):
    @api.doc('delete a tier')
    @admin_token_required
    def delete(self, id):
        """ Delete sme tier by id """
        tier = get_a_sme_tier(int(id))
        if tier is not None:
            delete_a_sme_tier(tier)
            return {'success': True}
        else:
            return {'success': False, 'msg': 'tier does not exist'}
