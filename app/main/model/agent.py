from .. import db
import datetime


class Agent(db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    location = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'), index=True)

    def __repr__(self):
        return '<Agent \'%s\'>' % self.name
