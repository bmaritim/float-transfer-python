from flask_restplus import Namespace, fields
from ..model import *


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class UploadDto:
    api = Namespace('upload', description='upload related operations')
    upload = api.model('upload_details', {
        'id': fields.Integer,
        'filename': fields.String(description='filename'),
        'url': fields.String(description='url '),
    })


class SmeAuthDto:
    api = Namespace('sme_auth', description='sme authentication related operations')
    sme_user_auth = api.model('sme_auth_details', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class OfficerAuthDto:
    api = Namespace('officer_auth', description='officer authentication related operations')
    officer_auth = api.model('officer_auth_details', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class IntranetAuthDto:
    api = Namespace('intranet_auth', description='intranet authentication related operations')
    intranet_auth = api.model('intranet_auth_details', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'password': fields.String(required=True, description='user password'),
        'phone': fields.String(description='user phone number'),
        'date_of_birth': fields.String(description='user date of birth'),
        'address': fields.String(description='user address'),
        'city': fields.String(description='user city'),
        'country': fields.String(description='user country'),
        'zip_code': fields.String(description='user zip code'),
        'status': fields.String(description='user status'),
        'business_name': fields.String(description='user business name'),
        'tin_no': fields.String(description='user tin number'),
        'image': fields.String(description='user image'),
        'amount_deposit': fields.String(description='user amount deposit'),
        'description': fields.String(description='user description'),
        'gender': fields.String(description='user gender'),
        'district': fields.String(description='user district'),
        'national_id': fields.String(description='national id'),
        'public_id': fields.String(description='user Identifier'),
        'role': fields.List(fields.Nested(api.model('role', {
            'id': fields.Integer,
            'name': fields.String(attribute='name')
        }))),
        'crypted_password': fields.String(description='crypted_password'),
        'salt': fields.String(description='salt'),
        'created_at': fields.String(description='created_at'),
        'updated_at': fields.String(description='updated_at'),
        'remember_me_token': fields.String(description='remember_me_token'),
        'reset_password_token': fields.String(description='reset_password_token'),
        'reset_password_email': fields.String(description='reset_password_email'),
        'email_flag': fields.String(description='email_flag'),
        'is_comm_include': fields.String(description='is_comm_include')
    })


class OfficerDto:
    api = Namespace('officer', description='officer related operations')
    officer = api.model('officer', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='officer email address'),
        'first_name': fields.String(required=True, description='officer first name'),
        'middle_name': fields.String(required=True, description=' middle name'),
        'last_name': fields.String(required=True, description='officer last name'),
        'password': fields.String(required=True, description='officer password'),
        'phone': fields.String(description='officer phone number'),
        'account': fields.Integer(description='officer account'),
        'birth': fields.String(description='officer date of birth'),
        'country_id': fields.Integer(required=True, description='officer country'),
        'town_id': fields.Integer(required=True, description='officer zip code'),
        'state': fields.String(description='officer state'),
        'status_type': fields.String(description='Status type', enum=StatusType._member_names_),
        'photo': fields.String(description='officer image'),
        'gender': fields.String(description='officer gender'),
        'district_id': fields.Integer(required=True, description='officer district')
    })


class CountryDto:
    api = Namespace('country', description='country related operations')
    country = api.model('country', {
        'id': fields.Integer,
        'name': fields.String(required=True, description='Country Name'),
        'districts': fields.List(fields.Nested(api.model('district', {
            'id': fields.Integer,
            'name': fields.String(attribute='name'),
            'towns': fields.List(fields.Nested(api.model('town', {
                'id': fields.Integer,
                'name': fields.String(attribute='name')
            })))
        })))
    })


class DistrictDto:
    api = Namespace('district', description='district related operations')
    district = api.model('district', {
        'id': fields.Integer,
        'name': fields.String(required=True, description='District Name'),
        'country_id': fields.Integer(required=True, description='District country'),
        'towns': fields.List(fields.Nested(api.model('town', {
            'id': fields.Integer,
            'name': fields.String(attribute='name')
        })))
    })


class TownDto:
    api = Namespace('town', description='town operations')
    town = api.model('town', {
        'id': fields.Integer,
        'name': fields.String(required=True, description='town Name'),
        'district_id': fields.Integer(required=True, description='town district')
    })


class MaintenanceOfficerDto:
    api = Namespace('maintenance_officer', description='maintenance officer related operations')
    maintenance_officer = api.model('maintenanceofficer', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='maintenance officer email address'),
        'first_name': fields.String(required=True, description='maintenance officer first name'),
        'middle_name': fields.String(required=True, description=' middle name'),
        'last_name': fields.String(required=True, description='last name'),
        'password': fields.String(required=True, description='password'),
        'phone': fields.String(description='phone number'),
        'account': fields.Integer(description='officer account'),
        'birth': fields.String(description='officer date of birth'),
        'country_id': fields.Integer(required=True, description='officer country'),
        'town_id': fields.Integer(required=True, description='officer zip code'),
        'state': fields.String(description='officer state'),
        'status_type': fields.String(description='Status type', enum=StatusType._member_names_),
        'photo': fields.String(description='officer image'),
        'gender': fields.String(description='officer gender'),
        'district_id': fields.Integer(required=True, description='officer district')
    })


class AggregatorDto:
    api = Namespace('aggregator', description='aggregator operations')
    aggregator = api.model('aggregator', {
        'id': fields.Integer,
        'aggregator_name': fields.String(required=True, description='aggregator name'),
        'contact_person_first_name': fields.String(description='contact person first_name'),
        'contact_person_last_name': fields.String(description='contact person last name'),
        'contact_person_phone': fields.String(description='contact person phone'),
        'commission_include': fields.Boolean(description='commission include'),
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'password': fields.String(required=True, description='user password'),
        'connection_timeout': fields.Float(description='Connection timeout')
    })


class RoleDto:
    api = Namespace('role', description='Role operations')
    role = api.model('role', {
        'id': fields.Integer,
        'name': fields.String(description='Role name'),
        'access_user': fields.Boolean(description='Access user'),
        'access_officer': fields.Boolean(description='Access officer'),
        'permissions': fields.Nested(api.model('permission', {
            'create_user': fields.Boolean(description='create user'),
            'read_user': fields.Boolean(description='read user'),
            'write_user': fields.Boolean(description='write user'),
            'delete_user': fields.Boolean(description='delete user'),
            'create_officer': fields.Boolean(description='create officer'),
            'read_officer': fields.Boolean(description='read officer'),
            'write_officer': fields.Boolean(description='write officer'),
            'delete_officer': fields.Boolean(description='delete officer')
        }))
    })


class SmeDto:
    api = Namespace('sme', description='sme related operations')
    sme = api.model('sme', {
        'id': fields.Integer,
        'status_type': fields.String(description='Status type', enum=SmeStatusType._member_names_),
        'business_name': fields.String(description='sme business name'),
        'tin': fields.String(description='sme tin number'),
        'type_of_service': fields.String(description='type_of_service'),
        'sme_tier': fields.Integer(description='tier'),
        'rdb_certificate': fields.String(description='rdb_certificate'),
        'tin_certificate': fields.String(description='tin_certificate'),
        'sme_compliance_cert': fields.String(description='sme_compliance_cert'),
        'id_copy': fields.String(description='id_copy'),
        'proof_of_payment': fields.String(description='proof_of_payment'),
        'country_id': fields.Integer(description='country'),
        'district_id': fields.Integer(description='district'),
        'town_id': fields.Integer(required=True, description='town'),
        'sme_location_category': fields.Integer(required=True, description='location category'),
    })


class AdminSmeDto:
    api = Namespace('sme', description='sme related operations')
    sme = api.model('sme', {
        'id': fields.Integer,
        'status_type': fields.String(description='Status type', enum=SmeStatusType._member_names_),
        'business_name': fields.String(description='sme business name'),
        'tin': fields.String(description='sme tin number'),
        'type_of_service': fields.String(description='type_of_service'),
        'sme_tier': fields.Integer(description='tier'),
        'rdb_certificate': fields.String(description='rdb_certificate'),
        'tin_certificate': fields.String(description='tin_certificate'),
        'sme_compliance_cert': fields.String(description='sme_compliance_cert'),
        'id_copy': fields.String(description='id_copy'),
        'proof_of_payment': fields.String(description='proof_of_payment'),
        'country_id': fields.Integer(description='country'),
        'district_id': fields.Integer(description='district'),
        'town_id': fields.Integer(required=True, description='town'),
        'sme_location_category': fields.Integer(required=True, description='location category'),
    })


class SmeUserDto:
    api = Namespace('sme_user', description='sme_user related operations')
    sme_user = api.model('sme_user', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'password': fields.String(required=True, description='user password'),
        'phone': fields.String(description='user phone number'),
        'date_of_birth': fields.String(description='user date of birth'),
        'address': fields.String(description='user address'),
        'city': fields.String(description='user city'),
        'country': fields.String(description='user country'),
        'zip_code': fields.String(description='user zip code'),
        'status': fields.String(description='user status'),
        'business_name': fields.String(description='user business name'),
        'tin_no': fields.String(description='user tin number'),
        'image': fields.String(description='user image'),
        'amount_deposit': fields.String(description='user amount deposit'),
        'description': fields.String(description='user description'),
        'gender': fields.String(description='user gender'),
        'district': fields.String(description='user district'),
        'national_id': fields.String(description='national id'),
        'public_id': fields.String(description='user Identifier'),
        'role': fields.List(fields.Nested(api.model('sme_role', {
            'id': fields.Integer,
            'name': fields.String(attribute='name')
        })))
    })


class SmeRoleDto:
    api = Namespace('sme_role', description='Role operations')
    sme_role = api.model('sme_role', {
        'id': fields.Integer,
        'name': fields.String(description='Role name'),
        'access_user': fields.Boolean(description='Access user'),
        'access_token': fields.Boolean(description='Access token'),
        'permissions': fields.Nested(api.model('sme_permission', {
            'create_user': fields.Boolean(description='create user'),
            'read_user': fields.Boolean(description='read user'),
            'write_user': fields.Boolean(description='write user'),
            'delete_user': fields.Boolean(description='delete user'),
            'create_token': fields.Boolean(description='create token'),
            'read_token': fields.Boolean(description='read token'),
            'write_token': fields.Boolean(description='write token'),
            'delete_token': fields.Boolean(description='delete token')
        }))
    })


class SmeLocationCategoryDto:
    api = Namespace('sme_role', description='Sme location category operations')
    sme_location_category = api.model('sme_location_category', {
        'id': fields.Integer,
        'name': fields.String(description='name')
    })


class SmeTierDto:
    api = Namespace('sme_tier', description='Sme tier operations')
    sme_tier = api.model('sme_tier', {
        'id': fields.Integer,
        'name': fields.String(description='name'),
        'amount': fields.String(description='amount')
    })


class MfDto:
    api = Namespace('mf', description='mf related operations')
    mf = api.model('mf', {
        'id': fields.Integer,
        'email': fields.String(required=True, description='mf email address'),
        'first_name': fields.String(required=True, description='mf first name'),
        'middle_name': fields.String(required=True, description='mf name'),
        'last_name': fields.String(required=True, description='mf last name'),
        'password': fields.String(required=True, description='mf password'),
        'phone': fields.String(description='mf phone number'),
        'tin': fields.String(description='mf tin number'),
        'account': fields.Integer(description='mf account'),
        'birth': fields.String(description='mf date of birth'),
        'country_id': fields.Integer(required=True, description='mf country'),
        'town_id': fields.Integer(required=True, description='mf zip code'),
        'state': fields.String(description='mf state'),
        'mf_status_type': fields.String(description='Status type', enum=StatusType._member_names_),
        'photo': fields.String(description='mf image'),
        'gender': fields.String(description='mf gender'),
        'district_id': fields.Integer(required=True, description='mf district'),
        'mf_deposits': fields.List(fields.Nested(api.model('mfdeposit', {
            'id': fields.Integer,
            'deposit_date': fields.String(attribute='deposit_date'),
            'deposit_amount': fields.String(attribute='deposit_amount'),
            'payment_mode': fields.String(attribute='payment_mode'),
            'reference_number': fields.String(attribute='reference_number')
        }))),
        'mf_credits': fields.List(fields.Nested(api.model('mfcredit', {
            'id': fields.Integer,
            'credit_date': fields.String(attribute='credit_date'),
            'credit_fee': fields.Nested(api.model('creditfeeconfig', {
                'id': fields.Integer,
                'fee': fields.String(attribute='fee'),
                'amount': fields.String(attribute='amount'),
                'approval_req': fields.String(attribute='approval_req')
            }))
        }))),
        'mf_penalties': fields.List(fields.Nested(api.model('mfpenalty', {
            'id': fields.Integer,
            'penalty_date': fields.String(attribute='penalty_date'),
            'penalty_fee': fields.Nested(api.model('mfpenaltyfee', {
                'id': fields.Integer,
                'penalty_type': fields.String(attribute='penalty_type'),
                'charges': fields.String(attribute='charges'),
                'is_active': fields.Boolean(attribute='is_active')
            }))
        }))),
        'mf_reimbursements': fields.List(fields.Nested(api.model('mfreimbursement', {
            'id': fields.Integer,
            'reimbursement_date': fields.String(attribute='reimbursement_date'),
            'reimbursement_amount': fields.String(attribute='reimbursement_amount')
        }))),
        'texts': fields.List(fields.Nested(api.model('sms', {
            'id': fields.Integer,
            'sms_id': fields.String(description='sms_id'),
            'cell_no': fields.String(description='cell_no'),
            'sms_date': fields.String(description='sms_date'),
            'sms_body': fields.String(description='sms_body'),
            'amount_received': fields.String(description='amount_received'),
            'generated_code': fields.String(description='generated_code'),
            'sms_sent': fields.Boolean(description='sms_sent'),
            'sms_error': fields.Boolean(description='sms_error'),
            'agent_confirmed': fields.Boolean(description='agent_confirmed')
        })))
    })


class MfDepositDto:
    api = Namespace('mf_deposit', description='mf deposit operations')
    mf_deposit = api.model('mfdeposit', {
        'id': fields.Integer,
        'deposit_date': fields.String(required=True, description='deposit_date'),
        'deposit_amount': fields.String(description='deposit_amount'),
        'payment_mode': fields.Integer(description='payment_mode'),
        'reference_number': fields.String(description='reference_number'),
        'mf_id': fields.Integer(required=True, description='mf')
    })


class MfCreditDto:
    api = Namespace('mf_credit', description='mf credit operations')
    mf_credit = api.model('mfcredit', {
        'id': fields.Integer,
        'credit_date': fields.String(required=True, description='credit_date'),
        'credit': fields.Nested(api.model('creditfeeconfig', {
            'id': fields.Integer,
            'fee': fields.Float(attribute='fee'),
            'amount': fields.Float(attribute='amount'),
            'approval_req': fields.String(attribute='approval_req')
        })),
        'mf_id': fields.Integer(required=True, description='mf')
    })


class MfPenaltyDto:
    api = Namespace('mf_penalty', description='mf penalty operations')
    mf_penalty = api.model('mfpenalty', {
        'id': fields.Integer,
        'penalty_date': fields.String(required=True, description='penalty_date'),
        'penalty': fields.Nested(api.model('mfpenaltyfee', {
            'id': fields.Integer,
            'penalty_type': fields.String(attribute='penalty_type'),
            'charges': fields.Float(attribute='charges'),
            'is_active': fields.Boolean(attribute='is_active')
        })),
        'mf_id': fields.Integer(required=True, description='mf')
    })


class MfReimbursementDto:
    api = Namespace('mf_reimbursement', description='mf reimbursement operations')
    mf_reimbursement = api.model('mfreimbursement', {
        'id': fields.Integer,
        'reimbursement_date': fields.String(required=True, description='reimbursement_date'),
        'reimbursement_amount': fields.String(description='reimbursement_amount'),
        'payment_mode': fields.Integer(description='payment_mode'),
        'reference_number': fields.String(description='reference_number'),
        'mf_id': fields.Integer(required=True, description='mf')
    })


class PaymentModeDto:
    api = Namespace('payment_mode', description='payment mode operations')
    payment_mode = api.model('paymentmode', {
        'id': fields.Integer,
        'payment_mode_type': fields.String(description='payment mode type'),
        'status': fields.Boolean(description='payment mode status')
    })


class PenaltyDto:
    api = Namespace('penalty', description='penalty operations')
    penalty = api.model('mfpenaltyfee', {
        'id': fields.Integer,
        'penalty_type': fields.String(description='penalty type'),
        'charges': fields.Float(description='penalty charges'),
        'is_active': fields.Boolean(description='penalty status')
    })


class CreditDto:
    api = Namespace('credit', description='credit operations')
    credit = api.model('creditfeeconfig', {
        'id': fields.Integer,
        'fee': fields.Float(description='credit fee'),
        'amount': fields.Float(description='credit amount'),
        'approval_req': fields.Boolean(description='approval')
    })


class LeasingDto:
    api = Namespace('leasing', description='leasing operations')
    leasing = api.model('leasingfee', {
        'id': fields.Integer,
        'fee_amount': fields.Float(description='fee_amount'),
        'applicable_from': fields.Float(description='applicable_from')
    })


class ServiceDto:
    api = Namespace('service', description='service operations')
    service = api.model('servicelist', {
        'id': fields.Integer,
        'service_name': fields.String(description='service name'),
        'service_type': fields.String(description='service type')
    })


class ServiceFeeDto:
    api = Namespace('service_fee', description='service operations')
    servicefee = api.model('servicefee', {
        'id': fields.Integer,
        'service': fields.List(fields.Nested(api.model('servicelist', {
            'id': fields.Integer,
            'service_type': fields.String(attribute='service_type'),
            'service_name': fields.String(attribute='service_name')
        }))),
        'total_comm_per': fields.Float(description='total_comm_per'),
        'total_comm_fix': fields.Float(description='total_comm_fix'),
        'our_comm_per': fields.Float(description='our_comm_per'),
        'our_comm_fix': fields.Float(description='our_comm_fix'),
        'agent_comm_per': fields.Float(description='agent_comm_per'),
        'agent_comm_fix': fields.Float(description='agent_comm_fix'),
        'effective_date': fields.String(description='effective_date'),
        'rate': fields.Float(description='rate'),
        'duration': fields.Float(description='duration'),
        'who_will_pay': fields.String(description='who_will_pay')
    })


class ServiceMasterDto:
    api = Namespace('service_fee_master', description='service master operations')
    service_master = api.model('servicefeesmaster', {
        'id': fields.Integer,
        'service': fields.Nested(api.model('servicelist', {
            'id': fields.Integer,
            'service_type': fields.String(attribute='service_type'),
            'service_name': fields.String(attribute='service_name')
        })),
        'effective_date': fields.String(description='effective_date'),
        'rate': fields.Float(description='rate'),
        'comm_payer': fields.String(description='commission_payer'),
        'vat_type': fields.String(description='vat_type')
    })


class ServiceSlaveDto:
    api = Namespace('service_fee_slave', description='service slave operations')
    service_master = api.model('servicefeesslab', {
        'id': fields.Integer,
        'master_id': fields.Integer,
        'comm_payer': fields.String(description='comm_payer'),
        'min_amount': fields.Float(description='min_amount'),
        'max_amount': fields.Float(description='max_amount'),
        'comm_type': fields.String(description='comm_type'),
        'total_comm': fields.Float(description='total_comm'),
        'our_comm': fields.Float(description='our_comm'),
        'agent_comm': fields.Float(description='agent_comm'),
        'sequence': fields.Integer(description='sequence'),
        'aggregator_comm': fields.Float(description='aggregator_comm')
    })


class KioskDto:
    api = Namespace('kiosk', description='kiosk operations')
    kiosk = api.model('kiosk', {
        'id': fields.Integer,
        'model': fields.String(description='model'),
        'purchase_date': fields.String(description='purchase_date'),
        'mf_id': fields.Integer(description='microfranchisee_id'),
        'condition': fields.String(description='condition')
    })


class SmsDto:
    api = Namespace('sms', description='text message operations')
    sms = api.model('sms', {
        'id': fields.Integer,
        'sms_id': fields.String(required=True, description='sms_id'),
        'cell_no': fields.String(description='cell_no'),
        'sms_date': fields.String(description='sms_date'),
        'sms_body': fields.String(description='sms_body'),
        'amount_received': fields.String(description='amount_received'),
        'generated_code': fields.String(description='generated_code'),
        'sms_sent': fields.Boolean(description='sms_sent'),
        'sms_error': fields.Boolean(description='sms_error'),
        'agent_confirmed': fields.Boolean(description='agent_confirmed'),
        'agent_id': fields.Integer(description='agent/mf')
    })


class IUserDto:
    api = Namespace('i_user', description='intranet user operations')
    i_user = api.model('_user', {
        'id': fields.Integer,
        'client_id': fields.Integer(description='client_id'),
        'utype_id': fields.Integer(description='utype_id'),
        'name': fields.String(description='name'),
        'email': fields.String(description='email'),
        'password': fields.String(description='password'),
        'user_status': fields.String(description='user_status')
    })


class BoxDto:
    api = Namespace('box', description='box operations')
    box = api.model('_box', {
        'id': fields.Integer,
        'box_name': fields.String(description='utype id'),
        'box_mac': fields.String(description='box_mac'),
        'box_folder': fields.String(description='box folder'),
        'location': fields.String(description='location'),
        'city': fields.String(description='city'),
        'zone_id': fields.String(description='zones'),
        'country_id': fields.Integer(description='country_id'),
        'box_status': fields.String(description='box status')
    })


class CategoryDto:
    api = Namespace('category', description='box operations')
    category = api.model('_category', {
        'id': fields.Integer,
        'category_name': fields.String(description='category name'),
        'category_status': fields.String(description='category status')
    })


class IUploadDto:
    api = Namespace('i_upload', description='intranet upload operations')
    i_upload = api.model('_upload', {
        'id': fields.Integer,
        'up_title': fields.String(description='up_title'),
        'up_poster': fields.String(description='up_poster'),
        'up_desc': fields.String(description='up_desc'),
        'up_attach': fields.String(description='up_attach'),
        'up_status': fields.String(description='up_status'),
        'category_id': fields.Integer(description='category_id')
    })


class ZoneDto:
    api = Namespace('zone', description='zone operations')
    zone = api.model('_zone', {
        'id': fields.Integer,
        'name': fields.String(description='name'),
        'country_id': fields.Integer(description='country_id'),
        'status': fields.Integer(description='status')
    })


class ICountryDto:
    api = Namespace('i_country', description='intranet country operations')
    i_country = api.model('_country', {
        'id': fields.Integer,
        'name': fields.String(description='name'),
        'status': fields.Integer(description='status')

    })


class ApiuserDto:
    api = Namespace('apiuser', description='payment operations')


class QuestionDto:
    api = Namespace('question', description='question operations')
    question = api.model('question', {
        'id': fields.Integer,
        'question': fields.String(required=True, description='question'),
        'answers': fields.List(fields.Nested(api.model('answer', {
            'id': fields.Integer,
            'answer': fields.String(attribute='answer')
        })))
    })


class AnswerDto:
    api = Namespace('answer', description='answer operations')
    answer = api.model('answer', {
        'id': fields.Integer,
        'answer': fields.String(required=True, description='answer'),
        'question_id': fields.Integer(required=True, description='question')
    })


class UserAnswerDto:
    api = Namespace('user_answer', description='user answers operations')
    user_answer = api.model('user_answer', {
        'id': fields.Integer,
        'answer': fields.String(required=True, description='answer'),
        'question_id': fields.Integer(required=True, description='question'),
        'mf_id': fields.Integer(required=True, description='microfranchisee'),
        'question': fields.Nested(api.model('question', {
            'id': fields.Integer,
            'question': fields.String(attribute='question'),
            'answer': fields.String(description='answer')
        }))
    })
