from .. import db, flask_bcrypt
import datetime


class Aggregator(db.Model):
    __tablename__ = 'aggregators'
    id = db.Column(db.Integer, primary_key=True)
    aggregator_name = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(100))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    connection_timeout = db.Column(db.Float)
    contact_person_first_name = db.Column(db.String(255))
    contact_person_last_name = db.Column(db.String(255))
    contact_person_phone = db.Column(db.String(255))
    commission_include = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Aggregator \'%s\'>' % self.aggregator_name
