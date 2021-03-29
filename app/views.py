# -*- coding:utf-8 -*-
from flask import flash, request, render_template

from app import app
from .emails import send_email
from .forms import ContactForm


@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):

    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    if request.method == 'POST':
        # honeybot https://stackoverflow.com/questions/36227376/better-honeypot-implementation-form-anti-spam
        if request.form.get('password'):
            print(len(request.form.getlist('contact_me')))
            return render_template('index.html', form=form)
        if form.validate():
            nom = request.form.get('nom')
            email = request.form.get('email')
            message = request.form.get('message')
            send_email(nom, email, message)
            flash('merci pour votre message', 'sucess')
            # return empty message
            message = form.message.data
            form.message.data = ''
            return render_template('index.html', form=form, message=message)
        else:
            flash('le formulaire comporte des erreurs', 'danger')
            return render_template('index.html', form=form)
