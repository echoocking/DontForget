from pykafka import KafkaClient
import json
kafka_client = KafkaClient(hosts='172.17.112.191:9092,172.17.112.192:9092,172.17.112.193:9092', use_greenlets=True, )
kafka_msg_topic = kafka_client.topics['product_incoming']
producer = kafka_msg_topic.get_sync_producer()

data = [
{"action": "u", "msg_tag": "price", "data": {"20448134": {"price_change_log_type_id": 2}}, "tbl": "product", "ids": [20448134]},
{"action": "u", "msg_tag": "price", "data": {"11419473": {"price_change_log_type_id": 2}}, "tbl": "product", "ids": [11419473]},
{"action": "u", "msg_tag": "price", "data": {"1050800": {"price_change_log_type_id": 2}}, "tbl": "product", "ids": [1050800]}
]
for d in data:
    producer.produce(json.dumps(d))