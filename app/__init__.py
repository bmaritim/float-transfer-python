from flask_restplus import Api
from flask import Blueprint

import os

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.upload_controller import api as upload_ns
from .main.controller.officer_controller import api as officer_ns
from .main.controller.officer_auth_controller import api as officer_auth_ns
from .main.controller.country_controller import api as country_ns
from .main.controller.district_controller import api as district_ns
from .main.controller.town_controller import api as town_ns
from .main.controller.maintenance_officer_controller import api as maintenance_ns
from .main.controller.aggregator_controller import api as aggregator_ns
from .main.controller.role_controller import api as role_ns
from .main.controller.sme_auth_controller import api as sme_auth_ns
from .main.controller.sme_user_controller import api as sme_user_ns
from .main.controller.sme_tier_controller import api as sme_tier_ns
from .main.controller.sme_location_category_controller import api as sme_location_cat_ns
from .main.controller.sme_controller import api as sme_ns
from .main.controller.admin_sme_controller import api as admin_sme_ns
from .main.controller.mf_controller import api as mf_ns
from .main.controller.credit_controller import api as credit_ns
from .main.controller.penalty_controller import api as penalty_ns
from .main.controller.mf_credit_controller import api as mf_credit_ns
from .main.controller.mf_penalty_controller import api as mf_penalty_ns
from .main.controller.payment_controller import api as payment_mode_ns
from .main.controller.leasing_controller import api as leasing_ns
from .main.controller.mf_deposit_controller import api as mf_deposit_ns
from .main.controller.mf_reimbursement_controller import api as mf_reimbursement_ns
from .main.controller.kiosk_controller import api as kiosk_ns
from .main.controller.sms_controller import api as sms_ns
from .main.controller.intranet.user_controller import api as i_user_ns
from .main.controller.intranet.box_controller import api as box_ns
from .main.controller.intranet.category_controller import api as category_ns
from .main.controller.intranet.upload_controller import api as i_upload_ns
from .main.controller.intranet.country_controller import api as i_country_ns
from .main.controller.intranet.zone_controller import api as zone_ns
from .main.controller.question_controller import api as question_ns
from .main.controller.answer_controller import api as answer_ns
from .main.controller.user_answer_controller import api as user_answer_ns

basedir = os.path.abspath(os.path.dirname(__file__))


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API',
          version='1.0',
          description='ARED API VERSION ONE'
          )


api.add_namespace(user_ns, path='/api/v1/user')
api.add_namespace(auth_ns, path='/api/v1/auth')
api.add_namespace(upload_ns, path='/api/v1/media')
api.add_namespace(sme_auth_ns, path='/api/v1/sme/auth')
api.add_namespace(officer_auth_ns, path='/api/v1/officer/auth')
api.add_namespace(officer_ns, path='/api/v1/officer')
api.add_namespace(country_ns, path='/api/v1/country')
api.add_namespace(district_ns, path='/api/v1/district')
api.add_namespace(town_ns, path='/api/v1/town')
api.add_namespace(maintenance_ns, path='/api/v1/maintenance_officer')
api.add_namespace(aggregator_ns, path='/api/v1/aggregator')
api.add_namespace(role_ns, path='/api/v1/role')
api.add_namespace(sme_user_ns, path='/api/v1/sme/user')
api.add_namespace(sme_tier_ns, path='/api/v1/sme/tier')
api.add_namespace(sme_location_cat_ns, path='/api/v1/sme/location_category')
api.add_namespace(sme_ns, path='/api/v1/sme')
api.add_namespace(admin_sme_ns, path='/api/v1/admin/sme')
api.add_namespace(mf_ns, path='/api/v1/microfranchisee')
api.add_namespace(mf_credit_ns, path='/api/v1/microfranchisee/credit')
api.add_namespace(mf_penalty_ns, path='/api/v1/microfranchisee/penalty')
api.add_namespace(credit_ns, path='/api/v1/credit')
api.add_namespace(penalty_ns, path='/api/v1/penalty')
api.add_namespace(payment_mode_ns, path='/api/v1/payment_mode')
api.add_namespace(leasing_ns, path='/api/v1/leasing_fee')
api.add_namespace(mf_deposit_ns, path='/api/v1/microfranchisee/deposit')
api.add_namespace(mf_reimbursement_ns, path='/api/v1/microfranchisee/reimbursement')
api.add_namespace(kiosk_ns, path='/api/v1/kiosk')
api.add_namespace(sms_ns, path='/api/v1/sms')
api.add_namespace(i_user_ns, path='/api/v1/intranet/user')
api.add_namespace(box_ns, path='/api/v1/intranet/device')
api.add_namespace(category_ns, path='/api/v1/intranet/category')
api.add_namespace(i_upload_ns, path='/api/v1/intranet/upload')
api.add_namespace(i_country_ns, path='/api/v1/intranet/country')
api.add_namespace(zone_ns, path='/api/v1/intranet/zone')
api.add_namespace(question_ns, path='/api/v1/question')
api.add_namespace(answer_ns, path='/api/v1/answer')
api.add_namespace(user_answer_ns, path='/api/v1/user_answer')
