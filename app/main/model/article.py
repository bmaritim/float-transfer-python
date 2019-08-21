from .. import db
import datetime


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String(1000))
    language = db.Column(db.String(255))
    file = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Article \'%s\'>' % self.title
