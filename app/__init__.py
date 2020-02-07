from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/diegocosta/Desktop/onovolab-flask/example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    
    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .api import bp_citys
    app.register_blueprint(bp_citys)

    return app