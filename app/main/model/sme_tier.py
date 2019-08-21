from .. import db
import datetime


class SmeTier(db.Model):
    __tablename__ = "sme_tiers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<SmeTier \'%s\'>' % self.name

