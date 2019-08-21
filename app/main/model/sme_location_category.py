from .. import db
import datetime


class SmeLocationCategory(db.Model):
    __tablename__ = "sme_location_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<SmeTierCategory \'%s\'>' % self.name
