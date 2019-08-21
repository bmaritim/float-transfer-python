from .. import db
import datetime


class SurveyResult(db.Model):
    __tablename__ = "survey_results"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kiosk_id = db.Column(db.Integer, db.ForeignKey('kiosks.id'), index=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'), index=True)
    survey_result_answers = db.relationship('SurveyResultAnswer', backref='surveyresult', lazy='dynamic')

    def __repr__(self):
        return '<SurveyResult \'%s\'>' % self.kiosk_id


