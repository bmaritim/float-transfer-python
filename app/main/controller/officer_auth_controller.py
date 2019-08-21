from flask import request
from flask_restplus import Resource

from app.main.service.officer_auth_helper import *
from ..util.dto import OfficerAuthDto

api = OfficerAuthDto.api
officer_auth = OfficerAuthDto.officer_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(officer_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return OfficerAuth.login_user(data=post_data)


@api.route('/verify')
class UserVerify(Resource):
    """
        User Verification Resource
    """
    @api.doc('user verification')
    def post(self):
        print(request)
        return OfficerAuth.get_logged_in_user(request)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return OfficerAuth.logout_user(data=auth_header)
