from .. import db
import datetime


class TxnHeader(db.Model):
    __tablename__ = 'txn_headers'
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(255))
    sub_type = db.Column(db.String(255))
    txn_date = db.Column(db.String(255))
    currency_code = db.Column(db.String(255))
    amount = db.Column(db.String(255))
    feeId = db.Column(db.String(255))
    agent_id = db.Column(db.String(255))
    agent_commission = db.Column(db.String(255))
    opt_commission = db.Column(db.String(255))
    total_commission = db.Column(db.String(255))
    status = db.Column(db.String(255))
    gateway = db.Column(db.String(255))
    initated_by = db.Column(db.String(255))
    description = db.Column(db.String(255))
    #account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    external_reference = db.Column(db.String(255))
    param1 = db.Column(db.String(255))
    unit = db.Column(db.String(255))
    vat = db.Column(db.String(255))
    electricity_costumer = db.Column(db.String(255))
    is_rollback = db.Column(db.String(255))
    area = db.Column(db.String(255))
    bill_no = db.Column(db.String(255))
    duration = db.Column(db.String(255))
    third_party_txn_id = db.Column(db.String(255))
    aggregator_comm = db.Column(db.String(255))
    agent_vat = db.Column(db.String(255))
    ared_vat = db.Column(db.String(255))
    vat_status = db.Column(db.String(255))
    customer_fee = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<TxnHeader \'%s\'>' % self.service_type
