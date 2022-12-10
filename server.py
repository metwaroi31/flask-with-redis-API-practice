from flask import Flask
from apps.sensor.views import sensor_blueprint

################
#    config    #
################


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    app.config["JSON_AS_ASCII"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    # app.config.from_pyfile("config.py")
    # app.static_url_path = 'static/'
    # Session(app)
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(sensor_blueprint)
