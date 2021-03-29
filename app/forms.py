from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired("Tapez votre Nom")])
    email = StringField('Email', validators=[DataRequired("Tapez votre email"), Email()])
    message = TextAreaField('Message', validators=[DataRequired("Tapez votre message")])
    #recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField('Envoyez')