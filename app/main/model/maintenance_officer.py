from .. import db, flask_bcrypt
import datetime
import enum


class StatusType(enum.Enum):
    DEFAULT = "0"
    DEPLOYED = "1"
    SUSPENDED = "2"
    TERMINATED = "3"


class MaintenanceOfficer(db.Model):
    __tablename__ = "maintenance_officers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(100))
    account = db.Column(db.Integer)
    status_type = db.Column(db.Enum("DEFAULT", "DEPLOYED", "SUSPENDED", "TERMINATED", name="StatusType",
                                    default="DEFAULT"))
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

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<MaintenanceOfficer \'%s\'>' % self.first_name

