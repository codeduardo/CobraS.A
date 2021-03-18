#modulos instalados
from flask import Flask,render_template,request,redirect,url_for,flash
from decouple import config
import smtplib

#modulos locales
from app import init_app
from app.migrate import init_db
from app.database import db,Formulario,Usuario
from forms import FormularioForm


app = init_app()
@app.route('/database')
def database():
    init_db()
    return 'base de datos creada corectamente'
    
@app.route('/',methods=['GET','POST'])
def inicio():
    formulario = Formulario()
    formularioForm = FormularioForm(obj=formulario)
    if request.method == 'POST':
        if formularioForm.validate_on_submit():
            formularioForm.populate_obj(formulario)
            
            message = '''
                                        NUEVO USUARIO INTERESADO
                                        ========================
            NOMBRES: {},
            APELLIDOS: {},
            EMAIL: {},
            CELULAR: {},
            MENSAJE: {}
            '''.format(formulario.nombres,formulario.apellidos,formulario.email,formulario.celular,formulario.mensaje)
            app.logger.debug(message)
            server  = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('agredu1234@gmail.com',config('PASSWORD'))

            server.sendmail('agredu1234@gmail.com','agredu1941@gmail.com', message)

            server.quit()

            app.logger.debug('correo enviado')
    
            db.session.add(formulario)
            db.session.commit()
            flash('Correo Enviado',category = 'success')
            
            return redirect(url_for('inicio'))

    return render_template('index.html',formularioForm = formularioForm)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/services')
def services():
    return render_template('services.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/contacto',methods = ['GET','POST'])
def contacto():
    formulario = Formulario()
    formularioForm = FormularioForm(obj=formulario)
    if request.method == 'POST':
        if formularioForm.validate_on_submit():
            formularioForm.populate_obj(formulario)
            
            db.session.add(formulario)
            db.session.commit()
            flash('Correo Enviado',category = 'success')
            return redirect(url_for('contacto'))

    return render_template('contacto.html',formularioForm = formularioForm)
    


if __name__ == '__main__':
    app.run(debug=True)