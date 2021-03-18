from flask import render_template,url_for,redirect,flash
from flask_login import login_required,current_user

from . import mails
from ..database import Usuario, Formulario,db

@mails.route('/')
@login_required
def home():
    formularios = Formulario.query.all()   
    
    return render_template('mails/home.html',formularios = formularios,username = current_user.username)

@mails.route('/detail/<int:id>')
def detail(id):
    formulario = Formulario.query.filter_by(id=id).first()
    return render_template('mails/detail.html',formulario=formulario)

@mails.route('/delete/<int:id>')
def delete(id):
    formulario = Formulario.query.filter_by(id=id).first()
    db.session.delete(formulario)
    db.session.commit()
    flash('mail eliminado',category='error')
    return redirect(url_for('mails.home'))
    
    
@mails.route('/done/<int:id>')
def done(id):
    formulario = Formulario.query.filter_by(id=id).first()
    formulario.done = not(formulario.done) 
    db.session.commit()
    return redirect(url_for('mails.home'))
    

    