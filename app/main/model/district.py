from .. import db
import datetime


class District(db.Model):
    __tablename__ = "districts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    towns = db.relationship('Town', backref='district', lazy='dynamic')

    def __repr__(self):
        return '<District \'%s\'>' % self.name

