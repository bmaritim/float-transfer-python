from .. import db
import datetime


class UserAnswer(db.Model):
    __tablename__ = 'user_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(255))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<UserAnswer \'%s\'>' % self.answer


