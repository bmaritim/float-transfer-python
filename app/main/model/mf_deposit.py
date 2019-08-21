from .. import db
import datetime


class MfDeposit(db.Model):
    __tablename__ = 'mf_deposits'
    id = db.Column(db.Integer, primary_key=True)
    deposit_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    deposit_amount = db.Column(db.String(255))
    payment_mode = db.Column(db.Integer, db.ForeignKey('payment_modes.id'))
    reference_number = db.Column(db.String(255))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))

    def __repr__(self):
        return '<MfDeposit \'%s\'>' % self.deposit_amount
