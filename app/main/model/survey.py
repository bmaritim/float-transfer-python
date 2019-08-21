from .. import db
import datetime


class Survey(db.Model):
    __tablename__ = "surveys"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)
    language = db.Column(db.String(255))
    survey_results = db.relationship('SurveyResult', backref='survey', lazy='dynamic')

    def __repr__(self):
        return '<Survey \'%s\'>' % self.title


