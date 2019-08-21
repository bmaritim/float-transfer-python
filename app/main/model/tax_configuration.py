from .. import db
import datetime


class TaxConfiguration(db.Model):
    __tablename__ = 'tax_configurations'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(255))
    percentage = db.Column(db.Float)
    effective_date = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __repr__(self):
        return '<TaxConfiguration \'%s\'>' % self.service
