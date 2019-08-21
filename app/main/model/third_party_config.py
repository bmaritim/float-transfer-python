from .. import db
import datetime


class ThirdPartyConfig(db.Model):
    __tablename__ = 'third_party_configs'
    id = db.Column(db.Integer, primary_key=True)
    party_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    connection_timeout = db.Column(db.Float)
    status = db.Column(db.String(255))

    def __repr__(self):
        return '<ThirdPartyConfig \'%s\'>' % self.party_name
