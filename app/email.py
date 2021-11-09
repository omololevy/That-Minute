from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to,**kwargs):
    subject_pref = 'The pitch'
    sender_email =  'levyomolo@student.moringaschool.com'

    email = Message(subject_pref+subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
