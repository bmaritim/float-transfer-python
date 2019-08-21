from .. import db
import datetime


class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String(1000))
    acc_type = db.Column(db.String(255))
    currency = db.Column(db.String(255))
    amount = db.Column(db.String(255))
    balance = db.Column(db.String(255))
    due_date = db.Column(db.String(255))
    non_payment_status = db.Column(db.Integer)
    credit_fee = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Loan \'%s\'>' % self.title


