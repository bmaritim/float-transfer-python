from .. import db
import datetime


class WifiList(db.Model):
    __tablename__ = 'wifi_list'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.String(255))
    amount = db.Column(db.String(255))

    def __repr__(self):
        return '<WifiList \'%s\'>' % self.duration
