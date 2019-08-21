from .. import db
import datetime


class AgentCommission(db.Model):
    __tablename__ = 'agent_commissions'
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(255))
    sub_type = db.Column(db.String(255))
    txn_date = db.Column(db.String(255))
    previous_balance = db.Column(db.String(255))
    post_balance = db.Column(db.String(255))
    #header_id = db.Column(db.Integer, db.ForeignKey('headers.id'))
    status = db.Column(db.String(255))
    payment_ref = db.Column(db.String(255))
    acc_balance = db.Column(db.String(255))
    loan = db.Column(db.String(255))
    penalty = db.Column(db.String(255))
    total_comm = db.Column(db.String(255))
    tax_percentage = db.Column(db.String(255))
    total_tax = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<AgentCommission \'%s\'>' % self.service_type




