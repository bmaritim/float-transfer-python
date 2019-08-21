from .. import db
import datetime


class AgentCreditLimit(db.Model):
    __tablename__ = 'agent_credit_limits'
    id = db.Column(db.Integer, primary_key=True)
    loan_capacity_date = db.Column(db.String(255))
    loan_amount = db.Column(db.String(255))
    status = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<AgentCreditLimit \'%s\'>' % self.loan_amount




