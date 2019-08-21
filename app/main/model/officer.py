from .. import db, flask_bcrypt
import datetime
import enum
from ..config import key
import jwt
from app.main.model.blacklist import BlacklistToken


class StatusType(enum.Enum):
    DEFAULT = "0"
    DEPLOYED = "1"
    SUSPENDED = "2"
    TERMINATED = "3"


class Officer(db.Model):
    __tablename__ = "officers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(100))
    account = db.Column(db.Integer)
    status_type = db.Column(db.Enum("DEFAULT", "DEPLOYED", "SUSPENDED", "TERMINATED", name="StatusType"), default="DEFAULT")
    first_name = db.Column(db.String(64), index=True)
    middle_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(64), index=True)
    birth = db.Column(db.String(64))
    photo = db.Column(db.String(255))
    state = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), index=True)
    gender = db.Column(db.String(64))
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), index=True)
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'), index=True)
    deployed_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), index=True)
    deployed_district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), index=True)
    deployed_town_id = db.Column(db.Integer, db.ForeignKey('towns.id'), index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(officer_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                'iat': datetime.datetime.utcnow(),
                'sub': officer_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __repr__(self):
        return '<Officer \'%s, %s\'>' % (self.first_name, self.status_type)

