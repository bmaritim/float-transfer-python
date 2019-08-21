from .. import db
import datetime


class TxnItem(db.Model):
    __tablename__ = 'txn_items'
    id = db.Column(db.Integer, primary_key=True)
    credit_amount = db.Column(db.Float)
    debit_amount = db.Column(db.Float)
    post_balance = db.Column(db.Float)
    previous_balance = db.Column(db.Float)
    fee_amt = db.Column(db.Float)
    fee_id = db.Column(db.Integer)
    account_id = db.Column(db.Integer)
    header_id = db.Column(db.Integer)
    role = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<TxnItem \'%s\'>' % self.account_id
