from .. import db, flask_bcrypt
import datetime


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    read_role = db.Column(db.Boolean, default=False)
    write_role = db.Column(db.Boolean, default=False)
    create_role = db.Column(db.Boolean, default=False)
    delete_role = db.Column(db.Boolean, default=False)
    read_user = db.Column(db.Boolean, default=False)
    write_user = db.Column(db.Boolean, default=False)
    create_user = db.Column(db.Boolean, default=False)
    delete_user = db.Column(db.Boolean, default=False)
    read_officer = db.Column(db.Boolean, default=False)
    write_officer = db.Column(db.Boolean, default=False)
    create_officer = db.Column(db.Boolean, default=False)
    delete_officer = db.Column(db.Boolean, default=False)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def permission_list():
        data = [
            'read_role', 'write_role', 'create_role', 'delete_role',
            'read_user', 'write_user', 'create_user', 'delete_user',
            'read_officer', 'write_officer', 'create_officer', 'delete_officer'
                ]
        return data

    def from_dict_first_registration(self):
        for field in Permission.permission_list():
            setattr(self, field, True)

    def from_dict(self, data):
        for field in Permission.permission_list():
            if field in data:
                setattr(self, field, data[field])
