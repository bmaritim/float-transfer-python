from .. import db, flask_bcrypt
import datetime
import enum


class MfStatusType(enum.Enum):
    DEFAULT = "0"
    DEPLOYED = "1"
    SUSPENDED = "2"
    TERMINATED = "3"


class Mf(db.Model):
    __tablename__ = "mfs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(100))
    account = db.Column(db.Integer)
    mf_status_type = db.Column(db.Enum("DEFAULT", "DEPLOYED", "SUSPENDED", "TERMINATED", name="MfStatusType"),
                               default="DEFAULT")
    first_name = db.Column(db.String(64), index=True)
    middle_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    tin_no = db.Column(db.String(64))
    registered_on = db.Column(db.String, nullable=False)
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
    mf_deposits = db.relationship('MfDeposit', backref='mf', lazy='dynamic')
    mf_credits = db.relationship('MfCredit', backref='mf', lazy='dynamic')
    mf_penalties = db.relationship('MfPenalty', backref='mf', lazy='dynamic')
    mf_reimbursements = db.relationship('MfReimbursement', backref='mf', lazy='dynamic')
    kiosks = db.relationship('Kiosk', backref='mf', lazy='dynamic')
    user_answers = db.relationship('UserAnswer', backref='mf', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Mf \'%s, %s\'>' % (self.first_name, self.mf_status_type)

