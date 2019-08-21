from flask import request
from flask_restplus import Resource

from app.main.util.decorator import *
from ..util.dto import *
from ..service.town_service import *
api = TownDto.api
_town = TownDto.town


@api.route('/all')
class TownList(Resource):
    @api.doc('list_of_registered_towns')
    @api.marshal_list_with(_town, envelope='data')
    def get(self):
        """List all towns"""
        return get_all_towns()


@api.route('/new')
class TownList(Resource):
    @api.expect(_town, validate=True)
    @api.response(201, 'town successfully created.')
    @api.doc('create a new town')
    @token_required
    def post(self):
        """Creates a new town """
        data = request.json
        return save_new_town(data=data)


@api.route('/<town_id>')
@api.param('town_id', 'The town identifier')
@api.response(404, 'town not found.')
class Town(Resource):
    @api.doc('get a town')
    @api.marshal_with(_town)
    def get(self, town_id):
        """get a town given its identifier"""
        town = get_a_town(town_id)
        if not town:
            return {'success': False, 'msg': 'town does not exist'}
        else:
            return town



