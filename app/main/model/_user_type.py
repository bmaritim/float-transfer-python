from .. import db
import datetime


class _UserType(db.Model):
    __tablename__ = "_user_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    utype_name = db.Column(db.String(255))
    add_status = db.Column(db.String(255))
    edit_status = db.Column(db.String(255))
    delete_status = db.Column(db.String(255))
    list_status = db.Column(db.String(255))
    utyp_status = db.Column(db.String(255))
    add_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<_UserType \'%s\'>' % self.utype_name




