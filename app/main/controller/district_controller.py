from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.district_service import *
api = DistrictDto.api
_district = DistrictDto.district


@api.route('/all')
class DistrictList(Resource):
    @api.doc('list_of_registered_districts')
    @admin_token_required
    @api.marshal_list_with(_district, envelope='data')
    def get(self):
        """List all districts"""
        return get_all_districts()


@api.route('/new')
class DistrictList(Resource):
    @api.expect(_district, validate=True)
    @api.response(201, 'district successfully created.')
    @api.doc('create a new district')
    @token_required
    def post(self):
        """Creates a new district """
        data = request.json
        return save_new_district(data=data)


@api.route('/<int:district_id>')
@api.param('district_id', 'The district identifier')
@api.response(404, 'district not found.')
class District(Resource):
    @api.doc('get a district')
    @token_required
    @api.marshal_with(_district)
    def get(self, district_id):
        """get a district given its identifier"""
        district = get_a_district(district_id)
        if not district:
            api.abort(404)
        else:
            return district



