from .. import db
import datetime


class UserGovtAccount(db.Model):
    __tablename__ = "user_govt_accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_type = db.Column(db.String(255), index=True)
    currency = db.Column(db.String(255))
    balance = db.Column(db.Float)
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<UserGovtAccount\'%s\'>' % self.account_type

