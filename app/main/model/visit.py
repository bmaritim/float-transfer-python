from .. import db
import datetime


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    fixed = db.Column(db.String(255))
    reason = db.Column(db.String(255))
    maintenance_officer_id = db.Column(db.Integer, db.ForeignKey('maintenance_officers.id'), index=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), index=True)

    def __repr__(self):
        return '<Visit \'%s\'>' % self.fixed
