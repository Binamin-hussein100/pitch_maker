from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#set FLASK_APP=flask_test.py
def create_app(config_name):
    
    app = Flask(__name__)
    
    #initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap = Bootstrap(app)
    mail.init_app(app)
    
    
    #app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    
    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')
    
    return app