from .. import db
import datetime


class AgentPenaltyDetail(db.Model):
    __tablename__ = 'agent_penalty_details'
    id = db.Column(db.Integer, primary_key=True)
    loan_amount = db.Column(db.String(255))
    penalty_amount = db.Column(db.String(255))
    pending_penalty_amount = db.Column(db.String(255))
    #header_id = db.Column(db.Integer, db.ForeignKey('headers.id'))
    non_payment_status = db.Column(db.String(255))
    penalty_type_id = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<AgentPenaltyDetail \'%s\'>' % self.loan_amount
