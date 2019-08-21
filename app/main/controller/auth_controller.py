from flask import request
from flask_restplus import Resource


from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from random import *

api = AuthDto.api
user_auth = AuthDto.user_auth
otp = randint(000000, 999999)


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


# @api.route('/verify_otp')
# class UserOtp(Resource):
#     """
#         User Otp Resource
#     """
#     @api.doc('user otp')
#     @api.expect(user_auth, validate=True)
#     def post(self):
#         # get the post data
#
#         post_data = request.json
#         return Auth.login_user(data=post_data)


@api.route('/verify')
class UserVerify(Resource):
    """
        User Verification Resource
    """
    @api.doc('user verification')
    def post(self):
        print(request)
        return Auth.get_logged_in_user(request)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)


# @api.route('/send_otp')
# class UserOtp(Resource):
#     """
#         Otp Verification Resource
#     """
#     @api.doc('user otp')
#     @api.expect(user_auth)
#     def post(self):
#         data = request.json
#         email = data["email"]
#
#         return Auth.send_otp(email)
