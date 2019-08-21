from .. import db
import datetime


class Kiosk(db.Model):
    __tablename__ = 'kiosks'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(255))
    purchase_date = db.Column(db.String(255))
    condition = db.Column(db.String(255))
    qr_code = db.Column(db.String(255))
    identifier = db.Column(db.String(255), index=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    firmware = db.Column(db.String(255))
    internet_pin = db.Column(db.String(255))
    last_online_at = db.Column(db.String(255))
    status = db.Column(db.JSON)
    description = db.Column(db.String(255))
    client_task = db.Column(db.JSON)
    os_info = db.Column(db.JSON)
    trusted = db.Column(db.Boolean)
    ca = db.Column(db.String(255))
    certificate = db.Column(db.String(255))
    private_key = db.Column(db.String(255))
    uuid = db.Column(db.String(255))
    gps_info = db.Column(db.JSON)
    wifi_info = db.Column(db.JSON)
    wifi_clients_info = db.Column(db.JSON)
    device_info_content = db.Column(db.JSON)
    device_info_db = db.Column(db.JSON)
    device_size_content = db.Column(db.Integer)

    wifi_bookings = db.relationship('WifiBooking', backref='kiosk', lazy='dynamic', cascade='all,delete-orphan')
    survey_results = db.relationship('SurveyResult', backref='kiosk', lazy='dynamic', cascade='all,delete-orphan')
    issues = db.relationship('Issue', backref='kiosk', lazy='dynamic', cascade='all,delete-orphan')
    ad_statistics = db.relationship('AdStatistic', backref='kiosk', lazy='dynamic', cascade='all,delete-orphan')
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    mf_id = db.Column(db.Integer, db.ForeignKey('mfs.id'))

    def __repr__(self):
        return '<Kiosk \'%s\'>' % self.identifier
