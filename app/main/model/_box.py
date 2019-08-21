from .. import db
import datetime


class Box(db.Model):
    __tablename__ = "_boxes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('_clients.id'), index=True)
    box_name = db.Column(db.String(255))
    box_mac = db.Column(db.String(255))
    box_folder = db.Column(db.String(255))
    location = db.Column(db.String(255))
    city = db.Column(db.String(255))
    zone_id = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey('_countries.id'), index=True)
    box_status = db.Column(db.String(255))
    add_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<Box \'%s\'>' % self.box_name

