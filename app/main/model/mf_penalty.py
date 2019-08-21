from .. import db
import datetime


class MfPenalty(db.Model):
    __tablename__ = 'mf_penalties'
    id = db.Column(db.Integer, primary_key=True)
    penalty_date = db.Column(db.String(255))
    mf_penalty_fee_id = db.Column(db.Integer, db.ForeignKey('mf_penalty_fees.id'))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))

    def __repr__(self):
        return '<MfPenalty \'%s\'>' % self.id
