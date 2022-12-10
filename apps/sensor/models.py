from apps import redis_client


class sensor_model():

    def __init__(self, data):
        for data_item in data['readings']:
            redis_client.lpush(
                data['id'] + 'timestamp',
                data_item['timestamp']
            )
            redis_client.lpush(data['id'] + 'count', data_item['count'])

    @staticmethod
    def get_count(item_id):
        length = redis_client.llen(item_id + 'count')
        count_res = 0
        for i in range(0, length):
            count = redis_client.lindex(item_id + 'count', i)
            count_res = count_res + int(count)
        return count_res

    @staticmethod
    def get_timestamp(item_id):
        length = redis_client.llen(item_id + 'timestamp')
        timestamp = redis_client.lindex(item_id + 'timestamp', length-1)
        return timestamp
