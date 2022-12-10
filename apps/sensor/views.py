from apps.sensor.repo import sensor_service
from flask import (
    request,
    Blueprint,
    jsonify
)
import json


sensor_blueprint = Blueprint("sensor", __name__, url_prefix="/sensor")


class sensor_route():

    @sensor_blueprint.route('', methods=['POST'])
    def create_data_sensor():
        try:
            data = json.loads(request.data)
            item = sensor_service.create_sensor_data(data)
            if item:
                return jsonify({'message': 'success'}), 200
            else:
                return jsonify({'error': 'wrong data format, try again'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @sensor_blueprint.route('/<uuid>', methods=['GET'])
    def get(
        uuid
    ):
        args = request.args
        if args.get('timestamp'):
            timestamp = sensor_service.fetch_timestamp(uuid)
            return jsonify({'latest_timestamp': str(timestamp)}), 200
        elif args.get('count'):
            count = sensor_service.fetch_cumulative_count(uuid)
            return jsonify({'cumulative_count': count}), 200
        return jsonify({'error': 'invalid input'}), 401
