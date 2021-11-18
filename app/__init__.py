from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from os import path



bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = '236d1ffbf7aa6933f300c626273e39ed'

    # Initializing flask extensions
    #login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     
    
    from .models import Event

    #create_database(app)

    # setting config
    return app

