from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length,Email

class FormularioForm(FlaskForm):
    nombres = StringField('nombres',validators=[DataRequired(),Length(min=5,max=40)])
    apellidos = StringField('apellidos',validators=[DataRequired(),Length(min=5,max=50)])
    email = StringField('email',validators=[DataRequired(), Email(),Length(min=5,max=50)])
    celular = IntegerField('celular',validators=[DataRequired()])
    mensaje = TextAreaField('',validators=[DataRequired(), Length(min=5,max=254)])
    
class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre: ',validators=[DataRequired(),Length(min=5,max=40)])
    username = StringField('Username: ',validators=[DataRequired(),Length(min=5,max=40)])
    password = PasswordField('Password: ',validators=[DataRequired(),Length(min=5,max=40)])
    submit = SubmitField('LOGIN')