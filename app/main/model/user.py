from flask import current_app
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    access_role = db.Column(db.Boolean, default=False)
    access_user = db.Column(db.Boolean, default=False)
    access_officer = db.Column(db.Boolean, default=False)
    permissions = db.relationship('Permission', backref='role', uselist=False, cascade='all,delete-orphan')
    users = db.relationship('User', backref='role', cascade='all,delete-orphan')

    @staticmethod
    def role_list():
        data = ['access_role', 'access_user', 'access_officer']
        return data

    def from_dict_first_registration(self):
        for field in Role.role_list():
            setattr(self, field, True)

    def from_dict(self, data):
        for field in Role.role_list():
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Role \'%s\'>' % self.name


kiosks_association = db.Table('kiosks_association',
                              db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                              db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                              db.Column('kiosk_id', db.Integer, db.ForeignKey('kiosks.id'))
                              )


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    confirmed = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(64), index=True)
    date_of_birth = db.Column(db.String(64))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    zip_code = db.Column(db.String(64))
    status = db.Column(db.String(64))
    business_name = db.Column(db.String(64))
    tin_no = db.Column(db.String(64))
    image = db.Column(db.String(64))
    amount_deposit = db.Column(db.String(64))
    description = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    district = db.Column(db.String(64))
    national_id = db.Column(db.String(64))
    user_role = db.Column(db.String(64))
    crypted_password = db.Column(db.String(255))
    salt = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    remember_me_token = db.Column(db.String(255))
    reset_password_token = db.Column(db.String(255))
    reset_password_email = db.Column(db.String(255))
    email_flag = db.Column(db.Boolean)
    is_comm_include = db.Column(db.Boolean)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user_accounts = db.relationship('UserAccount', backref='user', lazy='dynamic')
    govt_accounts = db.relationship('UserGovtAccount', backref='user', lazy='dynamic')
    suggestions = db.relationship('Suggestion', backref='user', lazy='dynamic')
    loans = db.relationship('Loan', backref='user', lazy='dynamic')
    txn_headers = db.relationship('TxnHeader', backref='user', lazy='dynamic')
    agent_credit_limits = db.relationship('AgentCreditLimit', backref='user', lazy='dynamic')
    agent_commisions = db.relationship('AgentCommission', backref='user', lazy='dynamic')
    agent_penalty_details = db.relationship('AgentPenaltyDetail', backref='user', lazy='dynamic')
    booths = db.relationship('Booth', backref='user', lazy='dynamic')
    wifi_bookings = db.relationship('WifiBooking', backref='user', lazy='dynamic')
    wifi_user_lists = db.relationship('WifiUserList', backref='user', lazy='dynamic')
    kiosks = db.relationship('Kiosk', secondary=kiosks_association, backref='user')
    role_histories = db.relationship('RoleHistory', backref='user', lazy='dynamic')
    pending_requests = db.relationship('PendingRequest', backref='user', lazy='dynamic')
    api_keys = db.relationship('ApiKey', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
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

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def generate_confirmation_token(self, expiration=604800):
        """Generate a confirmation token to email a new user."""

        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_email_change_token(self, new_email, expiration=3600):
        """Generate an email change token to email an existing user."""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def generate_password_reset_token(self, expiration=3600):
        """
        Generate a password reset change token to email to an existing user.
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def confirm_account(self, token):
        """Verify that the provided token is for this user's id."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def change_email(self, token):
        """Verify the new email for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        db.session.commit()
        return True

    def reset_password(self, token, new_password):
        """Verify the new password for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return "<User '{}'>".format(self.full_name())
