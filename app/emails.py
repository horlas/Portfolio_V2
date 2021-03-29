from flask_mail import Message
from flask import render_template
from app import mail
from config import ADMINS, MAIL_USERNAME


def send_email(nom, email, message):
    subject = "Nouveau message de {} depuis Portofolio". format(nom)
    msg = Message(subject, sender=MAIL_USERNAME, recipients=[ADMINS[0]])
    msg.body = render_template("email.txt", nom=nom, email=email, message=message )
    mail.send(msg)