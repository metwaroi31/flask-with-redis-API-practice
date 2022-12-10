from apps.sensor.models import sensor_model


class sensor_service():

    @staticmethod
    def create_sensor_data(data):
        try:
            data = sensor_model(data)
            return True
        except Exception:
            return False

    @staticmethod
    def fetch_timestamp(item_id):
        try:
            data_timestamp = sensor_model.get_timestamp(item_id)
            return data_timestamp
        except Exception:
            return False

    @staticmethod
    def fetch_cumulative_count(item_id):
        try:
            data_count = sensor_model.get_count(item_id)
            print (data_count)
            return data_count
        except Exception as e:
            print (str(e))
            return False
