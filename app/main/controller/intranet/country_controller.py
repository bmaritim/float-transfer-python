from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ...util.dto import *
from ...service.intranet.country_service import *
api = ICountryDto.api
_i_country = ICountryDto.i_country


@api.route('/all')
class CountryList(Resource):
    @api.doc('list_of_i_countries')
    @api.marshal_list_with(_i_country)
    @admin_token_required
    def get(self):
        """List all registered countries"""
        return get_all_countries()


@api.route('/<country_id>')
@api.param('country_id', 'The country identifier')
@api.response(404, 'country not found.')
class Country(Resource):
    @api.doc('get a country')
    @token_required
    @api.marshal_with(_i_country)
    def get(self, country_id):
        """get a country given its identifier"""
        le_i_country = get_a_country(country_id)
        if not le_i_country:
            return {'success': False, 'message': 'country not found'}
        else:
            return le_i_country


@api.route('/<country_id>/delete')
@api.param('country_id', 'The identifier')
@api.response(404, 'country not found.')
class Country(Resource):
    @api.doc('delete a country')
    @token_required
    def delete(self, country_id):
        """ Delete country by id """
        le_i_country = get_a_country(country_id)
        if not le_i_country:
            return {'success': False, 'msg': 'country does not exist'}
        else:
            return delete_a_country(country_id)
