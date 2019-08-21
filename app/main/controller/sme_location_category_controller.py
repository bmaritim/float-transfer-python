from flask import request
from flask_restplus import Resource

from app.main.util.sme_decorator import *
from app.main.util.decorator import *
from ..util.dto import SmeLocationCategoryDto
from ..service.sme_location_category_service import *

api = SmeLocationCategoryDto.api
_sme_location_category = SmeLocationCategoryDto.sme_location_category


@api.route('/')
class SmeTierList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_sme_location_category, envelope='data')
    def get(self):
        """List all registered sme location"""
        return get_all_sme_location_categories()

    @api.expect(_sme_location_category, validate=True)
    @api.response(201, 'Sme location category successfully created.')
    @api.doc('create a new sme location category')
    def post(self):
        """Creates a new sme tier """
        data = request.json
        return save_new_sme_location_category(data=data)


@api.route('/<id>')
@api.param('id', 'The location category identifier')
class SmeTier(Resource):
    @api.doc('get a sme')
    @api.marshal_with(_sme_location_category)
    def get(self, id):
        """get a sme location category given its identifier"""
        n_id = id if id.isdigit() else 0
        location_category = get_a_sme_location_category(n_id)
        if not location_category:
            return {'success': False, 'message': 'location category not found'}
        else:
            return location_category


@api.route('/<id>/delete')
@api.param('id', 'The location category identifier')
@api.response(404, 'Location category not found.')
class SmeTier(Resource):
    @api.doc('delete a location category')
    def delete(self, id):
        """ Delete sme location category by id """
        tier = get_a_sme_location_category(int(id))
        if tier is not None:
            delete_a_sme_location_category(tier)
            return {'success': True}
        else:
            return {'success': False, 'msg': 'location category does not exist'}
