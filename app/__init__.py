from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .database import db
from .auth import auth
from .message import message
from .models import UserModel

login_manager=LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(username):
    return UserModel.get(username)

def init_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(message)

    login_manager.init_app(app)
    return app
