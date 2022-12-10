from flask import (
    Blueprint,
)


sensor_blueprint = Blueprint("sensor", __name__, url_prefix="/sensor")
