from flask import Blueprint
from flask import request
from responses import good_data
import json
import pika


api = Blueprint('api', __name__)


@api.route('/send', methods=['POST'])
def send():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                   5672,
                                                                   '/',
                                                                   credentials))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    new_data = request.get_json()
    with open("answers.json", "w") as answers:
        json.dump(new_data, answers)
    channel.basic_publish(
        exchange='', routing_key='my_queue', body='answers.json')
    connection.close()
    return good_data
