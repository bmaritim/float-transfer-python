from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.aggregator_service import *
api = AggregatorDto.api
_aggregator = AggregatorDto.aggregator


@api.route('/all')
class AggregatorList(Resource):
    @api.doc('list_of_registered_aggregators')
    @admin_token_required
    @api.marshal_list_with(_aggregator, envelope='data')
    def get(self):
        """List all aggregators"""
        return get_all_aggregators()


@api.route('/new')
class AggregatorList(Resource):
    @api.expect(_aggregator, validate=True)
    @api.response(201, 'aggregator successfully created.')
    @api.doc('create a new aggregator')
    @token_required
    def post(self):
        """Creates a new aggregator """
        data = request.json
        return save_new_aggregator(data=data)


@api.route('/<int:aggregator_id>')
@api.param('aggregator_id', 'The aggregator identifier')
@api.response(404, 'aggregator not found.')
class Aggregator(Resource):
    @api.doc('get an aggregator')
    @token_required
    @api.marshal_with(_aggregator)
    def get(self, aggregator_id):
        """get a aggregator given its identifier"""
        aggregator = get_a_aggregator(aggregator_id)
        if not aggregator:
            return {'success': False, 'msg': 'aggregator does not exist'}
        else:
            return aggregator


@api.route('/<aggregator_id>/delete')
@api.param('aggregator_id', 'The aggregator identifier')
@api.response(404, 'Aggregator not found.')
class Aggregator(Resource):
    @api.doc('delete an aggregator')
    @token_required
    def delete(self, aggregator_id):
        """ Delete aggregator by id """
        le_aggregator = get_a_aggregator(aggregator_id)
        if not le_aggregator:
            return {'success': False, 'msg': 'aggregator does not exist'}
        else:
            db.session.delete(le_aggregator)
            db.session.commit()
            return {'success': True, 'message': 'officer deleted successfully'}


