from .. import db
import datetime


class Booth(db.Model):
    __tablename__ = 'booths'
    id = db.Column(db.Integer, primary_key=True)
    booth_model = db.Column(db.String(255))
    date_purchased = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Booth \'%s\'>' % self.booth_model





