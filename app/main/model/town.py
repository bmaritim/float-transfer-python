from .. import db
import datetime


class Town(db.Model):
    __tablename__ = "towns"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))

    def __repr__(self):
        return '<Town \'%s\'>' % self.name

