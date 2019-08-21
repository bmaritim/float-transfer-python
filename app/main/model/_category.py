from .. import db
import datetime


class ICategory(db.Model):
    __tablename__ = "_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('_clients.id'), index=True)
    category_name = db.Column(db.String(255))
    category_status = db.Column(db.String(255))
    add_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<ICategory \'%s\'>' % self.category_name



