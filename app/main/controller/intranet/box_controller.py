from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ...util.dto import *
from ...service.intranet.box_service import *
api = BoxDto.api
_box = BoxDto.box


@api.route('/all')
class BoxList(Resource):
    @api.doc('list_of_boxes')
    @admin_token_required
    @api.marshal_list_with(_box, envelope='data')
    def get(self):
        """List all registered boxes"""
        return get_all_boxes()


@api.route('/new')
class BoxList(Resource):
    @api.expect(_box, validate=True)
    @api.response(201, 'box successfully created.')
    @api.doc('create a new box')
    @token_required
    def post(self):
        """Creates a new box"""
        data = request.json
        return save_new_box(data=data)


@api.route('/<box_id>')
@api.param('box_id', 'The box identifier')
@api.response(404, 'box not found.')
class Box(Resource):
    @api.doc('get a box')
    @token_required
    @api.marshal_with(_box)
    def get(self, box_id):
        """get a box given its identifier"""
        le_box = get_a_box(box_id)
        if not le_box:
            return {'success': False, 'message': 'box not found'}
        else:
            return le_box


@api.route('/<box_id>/edit')
@api.param('box_id', 'The box identifier')
@api.response(404, 'box not found.')
class Box(Resource):
    @api.expect(_box, validate=False)
    @api.response(201, 'box successfully edited.')
    @api.doc('edit a new box')
    @token_required
    def put(self, box_id):
        """Edits a new box """
        le_box = get_a_box(box_id)
        if not le_box:
            return {'success': False, 'message': 'box not found'}
        data = request.json
        return edit_box(box_id, data=data)


@api.route('/<box_id>/delete')
@api.param('box_id', 'The box identifier')
@api.response(404, 'box not found.')
class Box(Resource):
    @api.doc('delete an box')
    @token_required
    def delete(self, box_id):
        """ Delete box by id """
        le_box = get_a_box(box_id)
        if not le_box:
            return {'success': False, 'msg': 'box does not exist'}
        else:
            return delete_a_box(box_id)
