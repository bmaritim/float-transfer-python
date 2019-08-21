import os
import unittest
import datetime
import uuid

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import Role, User, Permission


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


@manager.command
def setup_prod():
    """Runs the set-up needed for production."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    # Role.insert_roles()
    admin_query = Role.query.first()
    if admin_query is not None:
        return {'message': 'error'}
    role = Role(
        name='super_admin'
    )
    permission = Permission(role=role)
    role.from_dict_first_registration()
    role.permissions.from_dict_first_registration()
    
    if User.query.filter_by(email='irosh@test.com').first() is None:
        user = User(
            role=role,
            first_name='Mzee',
            last_name='Mzima',
            password='icon',
            admin=True,
            confirmed=True,
            email='irosh@test.com',
            registered_on=datetime.datetime.utcnow(),
            public_id=str(uuid.uuid4()),
            date_of_birth='09-09-1990',
            address='9090',
            city='city',
            country='country',
            zip_code='zip_code',
            status='status',
            business_name='business_name',
            tin_no='tin_no',
            image='image',
            amount_deposit='amount_deposit',
            description='description',
            gender='gender',
            district='district',
            national_id='national_id',
            user_role='admin'
        )
        db.session.add(role)
        db.session.commit()
        print('Added administrator {}'.format(user.full_name()))


if __name__ == '__main__':
    manager.run()
