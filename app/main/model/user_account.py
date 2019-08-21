from .. import db
import datetime


class UserAccount(db.Model):
    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_type = db.Column(db.String(255), index=True)
    currency = db.Column(db.String(255))
    balance = db.Column(db.Float)
    version_id = db.Column(db.Integer, db.ForeignKey('versions.id'), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<UserAccount\'%s\'>' % self.account_type

