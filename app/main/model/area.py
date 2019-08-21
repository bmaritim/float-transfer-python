from .. import db
import datetime


class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    ancestry = db.Column(db.String(255))

    articles = db.relationship('Article', backref='area', lazy='dynamic')
    surveys = db.relationship('Survey', backref='area', lazy='dynamic')
    ads = db.relationship('Ad', backref='area', lazy='dynamic')
    kiosks = db.relationship('Kiosk', backref='area', lazy='dynamic')

    def __repr__(self):
        return '<Area \'%s\'>' % self.title
