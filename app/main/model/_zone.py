from .. import db
import datetime


class Zone(db.Model):
    __tablename__ = "_zones"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('_countries.id'))
    name = db.Column(db.String(255))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Zone \'%s\'>' % self.name





