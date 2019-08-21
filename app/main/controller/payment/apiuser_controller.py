from flask import request
from flask_restplus import Resource
from ...util.dto import *
from ...service.payment.apiuser_service import *

api = ApiuserDto.api


@api.route('/apiuser')
class ApiList(Resource):
    @api.doc('create api user')
    def post(self):
        """create api user"""
        return create_api_user()


@api.route('/apiuser')
class ApiList(Resource):
    @api.doc('get api user')
    def post(self):
        return get_api_key()
