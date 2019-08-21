from functools import wraps
from flask import request, g
from app.main.service.sme_auth_helper import Auth
from app.main.model import *


def sme_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def sme_admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('role_id')
        if admin != 1:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated


def sme_role_access(_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            for field in Role.role_list():
                if field is _role:
                    data, status = Auth.get_logged_in_user(request)
                    c_data = data.get('data')
                    role_id = c_data.get('role_id')
                    role = Role.query.get_or_404(role_id)
                    if not getattr(role, field):
                        response_object = {
                            'status': 'fail',
                            'message': 'You have no access to this resource. Contact your administrator.'
                        }
                        return response_object, 401
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def sme_permission_access(_permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            for field in Permission.permission_list():
                if field is _permission:
                    data, status = Auth.get_logged_in_user(request)
                    c_data = data.get('data')
                    role_id = c_data.get('role_id')
                    role = Role.query.get_or_404(role_id)
                    if not getattr(role.permissions, field):
                        response_object = {
                            'status': 'fail',
                            'message': 'You have no access to this resource. Contact your administrator.'
                        }
                        return response_object, 401
            return f(*args, **kwargs)

        return decorated_function

    return decorator
