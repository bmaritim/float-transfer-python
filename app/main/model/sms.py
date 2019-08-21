from .. import db
import datetime


class Sms(db.Model):
    __tablename__ = 'texts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sms_id = db.Column(db.String(255))
    cell_no = db.Column(db.String(255))
    sms_date = db.Column(db.String(255))
    sms_body = db.Column(db.String(255))
    amount_received = db.Column(db.String(255))
    generated_code = db.Column(db.String(255))
    sms_sent = db.Column(db.Boolean)
    sms_error = db.Column(db.Boolean)
    agent_confirmed = db.Column(db.Boolean)
    agent_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Sms \'%s\'>' % self.sms_id

