from app.main import db
from app.main.model.sms import Sms
from app.main.model.mf_deposit import MfDeposit
from app.main.model.mf import Mf
import datetime


def save_new_sms(data):
    sms = Sms.query.filter_by(sms_id=data['sms_id']).first()
    if not sms:
        new_sms = Sms(
            sms_id=data['sms_id'],
            cell_no=data['cell_no'],
            sms_date=data['sms_date'],
            sms_body=data['sms_body'],
            amount_received=data['amount_received'],
            generated_code=data['generated_code'],
            sms_sent=data['sms_sent'],
            sms_error=data['sms_error'],
            agent_confirmed=data['agent_confirmed'],
            agent_id=data['agent_id']
        )
        save_changes(new_sms)
        return generate_new_sms(new_sms)
    else:
        response_object = {
            'status': 'fail',
            'message': 'sms already exists.'
        }
        return response_object, 409


def get_all_smss():
    return Sms.query.all()


def get_a_sms(sms_id):
    return Sms.query.get_or_404(sms_id)


def get_a_sms_by_code(generated_code):
    return Sms.query.filter_by(generated_code=generated_code).first()


def generate_new_sms(sms):
    try:
        response_object = {
            'success': 'true',
            'message': 'Sms Successfully Created.',
            'data': {
                'id': sms.id,
                'sms_id': sms.sms_id,
                'cell_no': sms.cell_no,
                'sms_date': sms.sms_date,
                'sms_body': sms.sms_body,
                'amount_received': sms.amount_received,
                'generated_code': sms.generated_code,
                'agent_id': sms.agent_id,
                'sms_sent': sms.sms_sent,
                'sms_error': sms.sms_error,
                'agent_confirmed': sms.agent_confirmed
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def check_token_code(generated_code):
    if generated_code:
        sms = get_a_sms_by_code(generated_code)
        initial_amount = int(sms.amount_received)
        final_amount = initial_amount * 0.99
        response_object = {
            'success': 'true',
            'message': 'Deposit amount received.',
            'data': {
                'new float deposit': final_amount
            }
        }
        return response_object, 201


def generate_new_mf_deposit(mf_deposit):
    try:
        response_object = {
            'success': 'true',
            'message': 'mf_deposit Successfully registered.',
            'data': {
                'mf_deposit_id': mf_deposit.id,
                'deposit_amount': mf_deposit.deposit_amount,
                'payment_mode': mf_deposit.payment_mode,
                'reference_number': mf_deposit.reference_number,
                'mf_id': mf_deposit.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def update_float(mf_deposit):
    try:
        response_object = {
            'success': 'true',
            'message': 'success.',
            'data': {
                'status': "Float deposited successfully",
                'message': 'success',
                'new_agent_float': mf_deposit.deposit_amount
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_an_sms(sms):
    db.session.delete(sms)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'sms Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

