from .. import db, flask_bcrypt
import datetime
import enum


class SmeStatusType(enum.Enum):
    PENDING = "0"
    APPROVED = "1"
    SUSPENDED = "2"
    TERMINATED = "3"


class Sme(db.Model):
    __tablename__ = "smes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_name = db.Column(db.String(100))
    sme_status_type = db.Column(db.Enum("PENDING", "APPROVED", "SUSPENDED", "TERMINATED", name="SmeStatusType"),
                                default="PENDING")
    tin = db.Column(db.String(255), index=True)
    sme_location_category = db.Column(db.Integer, db.ForeignKey('sme_location_categories.id'))
    type_of_service = db.Column(db.String(255))
    sme_tier = db.Column(db.Integer, db.ForeignKey('sme_tiers.id'))
    rdb_certificate = db.Column(db.String(255))
    tin_certificate = db.Column(db.String(255))
    sme_compliance_cert = db.Column(db.String(255))
    id_copy = db.Column(db.String(255))
    proof_of_payment = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), index=True)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), index=True)
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'), index=True)
    sme_user_id = db.Column(db.Integer, db.ForeignKey('sme_users.id'))

    def __repr__(self):
        return '<Sme \'%s, %s\'>' % (self.name, self.status_type)

