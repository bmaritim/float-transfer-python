from .. import db
import datetime


class Version(db.Model):
    __tablename__ = "versions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_type = db.Column(db.String(255))
    item_id = db.Column(db.Integer)
    event = db.Column(db.String(255))
    whodunnit = db.Column(db.String(255))
    object = db.Column(db.String(255))
    user_accounts = db.relationship('UserAccount', backref='version', lazy='dynamic')

    def __repr__(self):
        return '<Version \'%s\'>' % self.item_type

