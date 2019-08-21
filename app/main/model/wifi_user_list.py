from .. import db
import datetime


class WifiUserList(db.Model):
    __tablename__ = 'wifi_user_list'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.String(255))
    amount = db.Column(db.String(255))
    refer_code = db.Column(db.String(255))
    costumer_phone = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<WifiUserList \'%s\'>' % self.duration
