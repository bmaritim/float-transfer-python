from .. import db
import datetime


class WifiBooking(db.Model):
    __tablename__ = 'wifi_bookings'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.String(255))
    kind = db.Column(db.String(255))
    code = db.Column(db.String(255))
    start = db.Column(db.String(255))
    last_internet_ping = db.Column(db.String(25))
    mac_address = db.Column(db.String(255))
    kiosk_id = db.Column(db.Integer, db.ForeignKey('kiosks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<WifiBooking \'%s\'>' % self.duration
