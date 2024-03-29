from functools import wraps
from flask import request, g
from app.main.service.intranet_auth_helper import Auth
from app.main.model import *


def officer_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated

