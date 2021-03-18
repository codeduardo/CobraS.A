from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_fontawesome import FontAwesome

from .config import Config
from .database import db, Usuario





def init_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    app.config.from_object(Config)
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id ))
    
       
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
   
    from .mails import mails as mails_blueprint
    app.register_blueprint(mails_blueprint)

    return app
