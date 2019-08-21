from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ...util.dto import *
from ...service.intranet.zone_service import *
api = ZoneDto.api
_zone = ZoneDto.zone


@api.route('/all')
class ZoneList(Resource):
    @api.doc('list_of_zonees')
    @api.marshal_list_with(_zone, envelope='data')
    @admin_token_required
    def get(self):
        """List all registered zonees"""
        return get_all_zones()


@api.route('/<zone_id>')
@api.param('zone_id', 'The zone identifier')
@api.response(404, 'zone not found.')
class Zone(Resource):
    @api.doc('get a zone')
    @token_required
    @api.marshal_with(_zone)
    def get(self, zone_id):
        """get a zone given its identifier"""
        le_zone = get_a_zone(zone_id)
        if not le_zone:
            return {'success': False, 'message': 'zone not found'}
        else:
            return le_zone


@api.route('/<zone_id>/delete')
@api.param('zone_id', 'The zone identifier')
@api.response(404, 'zone not found.')
class Zone(Resource):
    @api.doc('delete a zone')
    @token_required
    def delete(self, zone_id):
        """ Delete zone by id """
        le_zone = get_a_zone(zone_id)
        if not le_zone:
            return {'success': False, 'msg': 'zone does not exist'}
        else:
            return delete_a_zone(zone_id)
