from .. import db
import datetime


class Upload(db.Model):
    __tablename__ = "_uploads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('_clients.id'), index=True)
    up_title = db.Column(db.String(255))
    up_poster = db.Column(db.String(255))
    up_desc = db.Column(db.String(255))
    up_attach = db.Column(db.String(255))
    up_status = db.Column(db.String(255))
    add_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<Upload \'%s\'>' % self.up_title


uploads_association = db.Table('uploads_association',
                               db.Column('upload_id', db.Integer, db.ForeignKey('_uploads.id')),
                               db.Column('category_id', db.Integer, db.ForeignKey('_categories.id'))
                               )
