from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ...util.dto import *
from ...service.intranet.category_service import *
api = CategoryDto.api
_category = CategoryDto.category


@api.route('/all')
class CategoryList(Resource):
    @api.doc('list_of_categories')
    @admin_token_required
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all registered categories"""
        return get_all_categories()


@api.route('/new')
class CategoryList(Resource):
    @api.expect(_category, validate=True)
    @api.response(201, 'category successfully created.')
    @api.doc('create a new category')
    @token_required
    def post(self):
        """Creates a new category"""
        data = request.json
        return save_new_category(data=data)


@api.route('/<category_id>')
@api.param('category_id', 'The category identifier')
@api.response(404, 'category not found.')
class Category(Resource):
    @api.doc('get a category')
    @token_required
    @api.marshal_with(_category)
    def get(self, category_id):
        """get a category given its identifier"""
        le_category = get_a_category(category_id)
        if not le_category:
            return {'success': False, 'message': 'category not found'}
        else:
            return le_category


@api.route('/<category_id>/edit')
@api.param('category_id', 'The category identifier')
@api.response(404, 'category not found.')
class Category(Resource):
    @api.expect(_category, validate=False)
    @api.response(201, 'category successfully edited.')
    @api.doc('edit a new category')
    @token_required
    def put(self, category_id):
        """Edits a new category """
        le_category = get_a_category(category_id)
        if not le_category:
            return {'success': False, 'message': 'category not found'}
        data = request.json
        return edit_category(category_id, data=data)


@api.route('/<category_id>/delete')
@api.param('category_id', 'The category identifier')
@api.response(404, 'category not found.')
class Category(Resource):
    @api.doc('delete an category')
    @token_required
    def delete(self, category_id):
        """ Delete category by id """
        le_category = get_a_category(category_id)
        if not le_category:
            return {'success': False, 'msg': 'category does not exist'}
        else:
            return delete_a_category(category_id)
