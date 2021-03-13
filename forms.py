from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class FormularioForm(FlaskForm):
    nombres = StringField('nombres',validators=[DataRequired()])
    apellidos = StringField('apellidos',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    celular = IntegerField('celular',validators=[DataRequired()])
    mensaje = TextAreaField('',validators=[DataRequired()])
    
