from flask import render_template,url_for,redirect


from . import mails

@mails.route('/home')
def home():
    render_template('mails/home.html')