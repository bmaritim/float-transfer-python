from .. import db
import datetime


class _Session(db.Model):
    __tablename__ = "_sessions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(255))
    expire = db.Column(db.DateTime)

    def __repr__(self):
        return '<_Session \'%s\'>' % self.data


