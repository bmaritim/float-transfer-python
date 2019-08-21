from .. import db
import datetime


class MfReimbursement(db.Model):
    __tablename__ = 'mf_reimbursements'
    id = db.Column(db.Integer, primary_key=True)
    reimbursement_date = db.Column(db.String(255))
    reimbursement_amount = db.Column(db.String(255))
    payment_mode = db.Column(db.Integer, db.ForeignKey('payment_modes.id'))
    reference_number = db.Column(db.String(255))
    status = db.Column(db.String(255))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))

    def __repr__(self):
        return '<MfReimbursement \'%s\'>' % self.reference_number

