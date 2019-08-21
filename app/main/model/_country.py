from .. import db
import datetime


class Country(db.Model):
    __tablename__ = "_countries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Integer)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Country \'%s\'>' % self.name


