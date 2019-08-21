from .. import db
import datetime


class _Client(db.Model):
    __tablename__ = "_clients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(255))
    client_status = db.Column(db.String(255))
    add_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<_Client \'%s\'>' % self.client_name


