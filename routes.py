from flask import Blueprint
from flask import request
from responses import good_data
import json
# import pika
from mock_answer import return_answer
import requests
from run import start

api = Blueprint('api', __name__)


# @api.route('/send', methods=['POST'])
# def send():
#     credentials = pika.PlainCredentials('guest', 'guest')
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
#                                                                    5672,
#                                                                    '/',
#                                                                    credentials))
#     channel = connection.channel()
#     channel.queue_declare(queue='my_queue')
#     new_data = request.get_json()
#     with open("answers.json", "w") as answers:
#         json.dump(new_data, answers)
#     channel.basic_publish(
#         exchange='', routing_key='my_queue', body='answers.json')
#     connection.close()
#     return good_data


@api.route('/mock-get-answers', methods=['GET'])
def mock():
    try:
        token = request.args.get('token')
        group_id = request.args.get('group_id')
        return return_answer(token=token, group_id=group_id)
    except:
        return "bad data"


@api.route('/change-active-bot', methods=['POST'])
def start_and_stop_bot():
    data = request.get_json()
    token = str(data['token'])
    group_id = str(data['group_id'])
    action = str(data['action'])
    answers = requests.get(url='http://localhost:5000/api/v1.0/mock-get-answers',
                           params={'token': token, 'group_id': group_id})
    answers = answers.json()
    start(answers, group_id, action)
    return good_data
