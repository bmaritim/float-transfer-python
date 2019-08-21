from .. import db
import datetime


class _BoxData(db.Model):
    __tablename__ = "_box_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    box_id = db.Column(db.Integer, db.ForeignKey('_boxes.id'), index=True)
    up_id = db.Column(db.Integer, db.ForeignKey('_uploads.id'), index=True)

    def __repr__(self):
        return '<_BoxData \'%s\'>' % self.box_id

