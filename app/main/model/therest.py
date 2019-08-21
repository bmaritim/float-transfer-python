from .. import db
import datetime


class SurveyResultAnswer(db.Model):
    __tablename__ = "survey_result_answers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_result_id = db.Column(db.Integer, db.ForeignKey('survey_results.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))

    def __repr__(self):
        return '<SurveyResultAnswer \'%s\'>' % self.survey_result_id


class Suggestion(db.Model):
    __tablename__ = "suggestions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255))
    user_comments = db.Column(db.String(255))
    admin_comments = db.Column(db.String(255))
    status = db.Column(db.String(255), default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Suggestion \'%s\'>' % self.type


class SmsRegistration(db.Model):
    __tablename__ = "sms_registrations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mobile_no = db.Column(db.String(255))
    purpose = db.Column(db.String(255))
    message = db.Column(db.String(255))
    deliver_on = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __repr__(self):
        return '<SmsRegistration \'%s\'>' % self.mobile_no


class ServiceSetting(db.Model):
    __tablename__ = "service_settings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service_lists.id'))
    balance = db.Column(db.Float, default=0.0)
    threshold_amount = db.Column(db.Float, default=0.0)
    emails = db.Column(db.String(255))
    notification_sent_date = db.Column(db.String(255))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<ServiceSetting \'%s\'>' % self.service


class ServiceList(db.Model):
    __tablename__ = "service_lists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(255))
    service_type = db.Column(db.String(255))

    def __repr__(self):
        return '<ServiceList \'%s\'>' % self.service_name


class ServiceFeesSlab(db.Model):
    __tablename__ = "service_fees_slabs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_id = db.Column(db.Integer, db.ForeignKey('service_fees_masters.id'))
    comm_payer = db.Column(db.String(255))
    min_amount = db.Column(db.Float)
    max_amount = db.Column(db.Float)
    comm_type = db.Column(db.String(255))
    total_comm = db.Column(db.Float)
    our_comm = db.Column(db.Float)
    agent_comm = db.Column(db.Float)
    sequence = db.Column(db.Integer)
    aggregator_comm = db.Column(db.Float, default=0.0)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<ServiceFeesSlab \'%s\'>' % self.master_id


class ServiceFeesMaster(db.Model):
    __tablename__ = "service_fees_masters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service_lists.id'))
    effective_date = db.Column(db.String(255))
    rate = db.Column(db.Float)
    comm_payer = db.Column(db.String(255))
    vat_type = db.Column(db.String(255))
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<ServiceFeesMaster \'%s\'>' % self.service


class ServiceFee(db.Model):
    __tablename__ = "service_fees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service_lists.id'))
    total_comm_per = db.Column(db.Float)
    total_comm_fix = db.Column(db.Float)
    our_comm_per = db.Column(db.Float)
    our_comm_fix = db.Column(db.Float)
    agent_comm_per = db.Column(db.Float)
    agent_comm_fix = db.Column(db.Float)
    effective_date = db.Column(db.String(255))
    rate = db.Column(db.Float, default=0.0)
    duration = db.Column(db.Integer, default=0)
    who_will_pay = db.Column(db.String(255))

    def __repr__(self):
        return '<ServiceFee \'%s\'>' % self.service


class SerialNumber(db.Model):
    __tablename__ = "serial_numbers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(255))
    active_flag = db.Column(db.Integer, default=0)
    gcm_key = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<SerialNumber \'%s\'>' % self.serial_number


class Score(db.Model):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metric = db.Column(db.String(255))
    target = db.Column(db.Integer, default=0)
    points = db.Column(db.String(255))
    scorable = db.Column(db.String(255))
    option = db.Column(db.String(255))
    interval = db.Column(db.String(255))

    def __repr__(self):
        return '<Score \'%s\'>' % self.metric


class RoleHistory(db.Model):
    __tablename__ = "role_histories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<RoleHistory \'%s\'>' % self.role_id


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'))
    agent_present = db.Column(db.Boolean)
    controller = db.Column(db.Boolean)
    wifi = db.Column(db.Boolean)
    replaced = db.Column(db.Boolean)
    clean = db.Column(db.Boolean)
    issue = db.Column(db.Boolean)
    summary_type = db.Column(db.String(255))
    summary_text = db.Column(db.String(255))
    kiosk_master_id = db.Column(db.Integer, db.ForeignKey('kiosk_masters.id'))

    def __repr__(self):
        return '<Review \'%s\'>' % self.issue


class QuickTeller(db.Model):
    __tablename__ = "quick_tellers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_amount_fixed = db.Column(db.Boolean)
    payment_item_id = db.Column(db.Integer)
    payment_item_name = db.Column(db.Integer)
    payment_code = db.Column(db.String(255))
    status = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    biller_id = db.Column(db.Integer)

    def __repr__(self):
        return '<QuickTeller \'%s\'>' % self.payment_item_id


class PendingRequest(db.Model):
    __tablename__ = "pending_requests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    txn_id = db.Column(db.String(255))
    service_type = db.Column(db.String(255))
    sub_type = db.Column(db.String(255))
    client_number = db.Column(db.String(255))
    amount = db.Column(db.Float)
    status = db.Column(db.Integer)
    txn_date = db.Column(db.Integer)
    remote_ip = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<PendingRequest \'%s\'>' % self.txn_id


class PendingLeasingFee(db.Model):
    __tablename__ = "pending_leasing_fees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    end_period = db.Column(db.String(255))
    payment_amount = db.Column(db.Float)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<PendingLeasingFee \'%s\'>' % self.agent_id


class PendingCredit(db.Model):
    __tablename__ = "pending_credits"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    txn_date = db.Column(db.String(255))
    approval_date = db.Column(db.String(255))
    amount = db.Column(db.Float)
    app_unique_id = db.Column(db.String)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<PendingCredit \'%s\'>' % self.agent_id


class PaymentMode(db.Model):
    __tablename__ = "payment_modes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment_mode_type = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<PaymentMode \'%s\'>' % self.payment_mode_type


class OneTimePassword(db.Model):
    __tablename__ = "one_time_passwords"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    otp_id = db.Column(db.String(255))
    otp = db.Column(db.String(255))
    description = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<OneTimePassword \'%s\'>' % self.otp_id


class NotificationNews(db.Model):
    __tablename__ = "notification_news"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    notification_content = db.Column(db.String(255))
    notification_title = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    read_flag = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<NotificationNews \'%s\'>' % self.notification_title


class MfPenaltyFee(db.Model):
    __tablename__ = "mf_penalty_fees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    penalty_type = db.Column(db.String(255))
    charges = db.Column(db.Float)
    is_active = db.Column(db.Boolean)
    status = db.Column(db.Boolean)

    def __repr__(self):
        return '<MfPenaltyFee \'%s\'>' % self.penalty_type


class LoanRating(db.Model):
    __tablename__ = "loan_ratings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Float)
    date = db.Column(db.String(255))
    parameter = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<LoanRating \'%s\'>' % self.user_id


class LeasingFee(db.Model):
    __tablename__ = "leasing_fees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    applicable_from = db.Column(db.String(255))
    fee_amount = db.Column(db.Float)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<LeasingFee \'%s\'>' % self.fee_amount


class KioskUser(db.Model):
    __tablename__ = "kiosk_users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kiosk_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<KioskUser \'%s\'>' % self.kiosk_id


class KioskMaster(db.Model):
    __tablename__ = "kiosk_masters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_no = db.Column(db.String(255))
    serial_no = db.Column(db.String(255))
    purchase_date = db.Column(db.String(255))
    qr_code_no = db.Column(db.String(255))
    functional_status = db.Column(db.String(255))
    status = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255))

    def __repr__(self):
        return '<KioskMaster \'%s\'>' % self.model_no


class KioskAgent(db.Model):
    __tablename__ = "kiosk_agents"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kiosk_master_id = db.Column(db.Integer, db.ForeignKey('kiosk_masters.id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    assign_status = db.Column(db.String(255))
    functional_status = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    status = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255))

    def __repr__(self):
        return '<KioskAgent \'%s\'>' % self.kiosk_master_id


class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kiosk_id = db.Column(db.Integer, db.ForeignKey('kiosks.id'))
    title = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    category = db.Column(db.Integer)
    description = db.Column(db.String(255))
    report = db.Column(db.String(255))
    pending_at = db.Column(db.String(255))
    closing_at = db.Column(db.String(255))

    def __repr__(self):
        return '<Issue \'%s\'>' % self.title


class GcmNot(db.Model):
    __tablename__ = "gcm_nots"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gcm_key = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<GcmNot \'%s\'>' % self.gcm_key


class GcmNotNews(db.Model):
    __tablename__ = "gcm_no_newss"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gcm_key = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<GcmNotNews \'%s\'>' % self.gcm_key


class GatewayLog(db.Model):
    __tablename__ = "gateway_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    log_id = db.Column(db.Integer)
    header_id = db.Column(db.String(255))
    aggregator_balance = db.Column(db.Float)
    aggregator_name = db.Column(db.String(255))
    txn_amount = db.Column(db.Float)
    request = db.Column(db.String(255))
    response = db.Column(db.String(255))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<GatewayLog \'%s\'>' % self.agent_id


class Firmware(db.Model):
    __tablename__ = "firmwares"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    file = db.Column(db.String(255))
    version = db.Column(db.String(255))
    revision = db.Column(db.String(255))
    distribution = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    areas_firmwares = db.relationship('AreasFirmware', backref='firmware', lazy='dynamic')

    def __repr__(self):
        return '<Firmware \'%s\'>' % self.title


class Deployment(db.Model):
    __tablename__ = "deployments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'))
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'))
    maintenance_officer_id = db.Column(db.Integer, db.ForeignKey('maintenance_officers.id'))

    def __repr__(self):
        return '<Deployment \'%s\'>' % self.country_id


class CreditSuspend(db.Model):
    __tablename__ = "credit_suspends"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    is_blocked = db.Column(db.Boolean)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<CreditSuspend \'%s\'>' % self.agent_id


class CreditFeeConfig(db.Model):
    __tablename__ = "credit_fees_configs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fee = db.Column(db.Float)
    amount = db.Column(db.Float)
    approval_req = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<CreditFeeConfig \'%s\'>' % self.amount


class AreasFirmware(db.Model):
    __tablename__ = "areas_firmwares"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    firmware_id = db.Column(db.Integer, db.ForeignKey('firmwares.id'))

    def __repr__(self):
        return '<AreasFirmware \'%s\'>' % self.area_id


class ApiKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    api_key = db.Column(db.String(255))
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<ApiKey \'%s\'>' % self.api_key


class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    announcement = db.Column(db.String(255))
    status = db.Column(db.Integer)
    txn_date = db.Column(db.String(255))
    created_by = db.Column(db.Integer)

    def __repr__(self):
        return '<Announcement \'%s\'>' % self.announcement


class AggregatorReconciliation(db.Model):
    __tablename__ = "aggregator_reconciliations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_type = db.Column(db.String(255))
    sub_type = db.Column(db.String(255))
    txn_amount = db.Column(db.Float)
    net_amount = db.Column(db.Float)
    total_commission = db.Column(db.Float)
    previous_balance = db.Column(db.Float)
    post_balance = db.Column(db.Float)
    status = db.Column(db.Integer)
    txn_date = db.Column(db.String(255))

    def __repr__(self):
        return '<AggregatorReconciliation \'%s\'>' % self.service_type


class Ad(db.Model):
    __tablename__ = "ads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))
    clicks = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    language = db.Column(db.String(255))
    link = db.Column(db.Integer)
    position = db.Column(db.Integer)
    ad_statistics = db.relationship('AdStatistic', backref='ad', lazy='dynamic', cascade='all,delete-orphan')

    def __repr__(self):
        return '<Ad \'%s\'>' % self.title


class AdStatistic(db.Model):
    __tablename__ = "ad_statistics"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('ads.id'))
    kiosk_id = db.Column(db.Integer, db.ForeignKey('kiosks.id'))
    access_logs_id = db.Column(db.Integer, db.ForeignKey('access_logs.id'))


    def __repr__(self):
        return '<AdStaistic\'%s\'>' % self.ad_id


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    action = db.Column(db.String(255))
    initiator = db.Column(db.String(255))
    description = db.Column(db.String(255))
    params = db.Column(db.String(255))

    def __repr__(self):
        return '<ActivityLog\'%s\'>' % self.action


class AccessLog(db.Model):
    __tablename__ = "access_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    remote_ip = db.Column(db.String(255))
    role = db.Column(db.Integer)
    is_successful = db.Column(db.Boolean)
    use_web = db.Column(db.Integer)
    status = db.Column(db.Integer)
    ad_statistics = db.relationship('AdStatistic', backref='accesslog', lazy='dynamic', cascade='all,delete-orphan')

    def __repr__(self):
        return '<AccessLog \'%s\'>' % self.access_id
