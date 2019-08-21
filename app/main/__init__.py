from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_qrcode import QRcode
from flask_mail import Mail, Message


from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
cors = CORS()
qrcode = QRcode()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    qrcode.init_app(app)
    mail.init_app(app)

    return app

