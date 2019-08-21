from .. import db
import datetime


class Upload(db.Model):
    __tablename__ = "uploads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), index=True)
    filename = db.Column(db.String(255))
    description = db.Column(db.String(255))
    language = db.Column(db.String(255))
    url = db.Column(db.String(255))

    def __repr__(self):
        return '<Upload\'%s\'>' % self.filename

