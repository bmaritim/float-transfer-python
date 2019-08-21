from .. import db
import datetime


class TransactionCategory(db.Model):
    __tablename__ = 'transaction_categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255))
    category_sub_name = db.Column(db.String(255))

    def __repr__(self):
        return '<TransactionCategory \'%s\'>' % self.category_name
