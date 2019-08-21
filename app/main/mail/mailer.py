import os
from flask_mail import Message
from app.main import mail
from threading import Thread
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients):
    msg = Message(subject, sender=sender, recipients=recipients)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


def send_otp(user):
    send_email('ARED OTP',
               sender=app.config['ADMIN_EMAIL'][0],
               recipients=[user.email]
               )
