from database import db

class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(80))
    celular=db.Column(db.Integer())
    mensaje = db.Column(db.String(255))
    
    