from .. import db
import datetime


class _Setting(db.Model):
    __tablename__ = "_settings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(255))
    key = db.Column(db.String(255))
    value = db.Column(db.String(255))
    serialized = db.Column(db.String(255))

    def __repr__(self):
        return '<_Setting \'%s\'>' % self.code



