from app.main import db
from app.main.model.aggregator import Aggregator


def save_new_aggregator(data):
    aggregator = Aggregator.query.filter_by(email=data['email']).first()
    if not aggregator:
        new_aggregator = Aggregator(
            aggregator_name=data['aggregator_name'],
            contact_person_first_name=data['contact_person_first_name'],
            contact_person_last_name=data['contact_person_last_name'],
            contact_person_phone=data['contact_person_phone'],
            commission_include=data['commission_include'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password'],
            connection_timeout=data['connection_timeout']
        )
        save_changes(new_aggregator)
        return generate_new_aggregator(new_aggregator)
    else:
        response_object = {
            'status': 'fail',
            'message': 'aggregator already exists.'
        }
        return response_object, 409


def get_all_aggregators():
    return Aggregator.query.all()


def get_a_aggregator(aggregator_id):
    return Aggregator.query.get_or_404(aggregator_id)


def generate_new_aggregator(aggregator):
    try:
        response_object = {
            'status': 'success',
            'message': 'aggregator Successfully registered.',
            'data': {
                'aggregator_id': aggregator.id,
                'aggregator_name': aggregator.aggregator_name,
                'contact_person_first_name': aggregator.contact_person_first_name,
                'contact_person_last_name': aggregator.contact_person_last_name,
                'contact_person_phone': aggregator.contact_person_phone,
                'commission_include': aggregator.commission_include,
                'email': aggregator.email,
                'first_name': aggregator.first_name,
                'last_name': aggregator.last_name,
                'connection_timeout': aggregator.connection_timeout
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_aggregator(aggregator_id):
    aggregator = get_a_aggregator(aggregator_id)
    if not aggregator:
        return {'success': 'fail', 'message': 'no such aggregator fam'}
    db.session.delete(aggregator)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Aggregator Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_aggregator(data):
    aggregator = Aggregator.query.filter_by(email=data['email']).first()
    if not aggregator:
        response_object = {
            'status': 'fail',
            'message': 'aggregator does not exist.'
        }
        return response_object, 409
    else:
        new_aggregator = Aggregator(
            aggregator_name=data['aggregator_name'],
            contact_person_first_name=data['contact_person_first_name'],
            contact_person_last_name=data['contact_person_last_name'],
            contact_person_phone=data['contact_person_phone'],
            commission_include=data['commission_include'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password'],
            connection_timeout=data['connection_timeout']
        )
        save_changes(new_aggregator)
        return update_aggregator(new_aggregator)


def update_aggregator(aggregator):
    try:
        response_object = {
            'status': 'success',
            'message': 'aggregator Successfully updated.',
            'data': {
                'aggregator_id': aggregator.id,
                'aggregator_name': aggregator.aggregator_name,
                'contact_person_first_name': aggregator.contact_person_first_name,
                'contact_person_last_name': aggregator.contact_person_last_name,
                'contact_person_phone': aggregator.contact_person_phone,
                'commission_include': aggregator.commission_include,
                'email': aggregator.email,
                'first_name': aggregator.first_name,
                'last_name': aggregator.last_name,
                'connection_timeout': aggregator.connection_timeout
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

