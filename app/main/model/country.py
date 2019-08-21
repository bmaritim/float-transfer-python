from .. import db
import datetime


class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    districts = db.relationship('District', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country \'%s\'>' % self.name

