from .. import db
import datetime


class MfCredit(db.Model):
    __tablename__ = 'mf_credits'
    id = db.Column(db.Integer, primary_key=True)
    credit_date = db.Column(db.String(255))
    status = db.Column(db.String(255))
    credit_fees_configs_id = db.Column(db.Integer, db.ForeignKey('credit_fees_configs.id'))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))

    def __repr__(self):
        return '<MfCredit \'%s\'>' % self.id
