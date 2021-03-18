from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(250))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        check_password_hash(self.password, password)


class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(80))
    celular = db.Column(db.Integer())
    mensaje = db.Column(db.String(255))
