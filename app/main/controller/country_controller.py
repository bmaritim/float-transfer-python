from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.country_service import *
api = CountryDto.api
_country = CountryDto.country


@api.route('/all')
class CountryList(Resource):
    @api.doc('list_of_registered_officers')
    @admin_token_required
    @api.marshal_list_with(_country, envelope='data')
    def get(self):
        """List all countries"""
        return get_all_countries()


@api.route('/new')
class CountryList(Resource):
    @api.expect(_country, validate=True)
    @api.response(201, 'country successfully created.')
    @api.doc('create a new country')
    @token_required
    def post(self):
        """Creates a new country """
        data = request.json
        return save_new_country(data=data)


@api.route('/<int:country_id>')
@api.param('country_id', 'The country identifier')
@api.response(404, 'country not found.')
class Country(Resource):
    @api.doc('get a country')
    @token_required
    @api.marshal_with(_country)
    def get(self, country_id):
        """get a officer given its identifier"""
        country = get_a_country(country_id)
        if not country:
            api.abort(404)
        else:
            return country


@api.route('/<int:country_id>/delete')
@api.param('country_id', 'The country identifier')
@api.response(404, 'country not found.')
class Country(Resource):
    @api.doc('delete a country')
    @token_required
    def delete(self, country_id):
        """ Delete country by id """
        le_country = get_a_country(country_id)
        if not le_country:
            return {'success': False, 'msg': 'country does not exist'}
        else:
            delete_a_country(country_id)
            return {'success': True, 'message': 'country deleted successfully'}

