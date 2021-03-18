from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .database import db





def init_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)
   
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
   
    from .mails import mails as mails_blueprint
    app.register_blueprint(mails_blueprint)

    return app
