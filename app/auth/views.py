from flask import render_template,flash,redirect, url_for,flash
from forms import LoginForm
from flask_login import login_user,login_required,logout_user


from ..database import Usuario
from . import auth


@auth.route('/login',methods = ['GET','POST'])

def login():
    login_form =LoginForm() 
    
    if login_form.validate_on_submit():
        usuario = Usuario.query.filter_by(username = login_form.username.data).first()
        if usuario :
            if usuario.check_password(login_form.password.data):
                login_user(usuario)
                flash('Bienvenido',category = 'success')
                return redirect(url_for('mails.home'))
        
        flash('usuario o contraseña invalida',category='error')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html',login_form = login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión Cerrada', category='success')
    return redirect(url_for('inicio'))