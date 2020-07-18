import pika
from vk import Answer
import json
from time import sleep


def check_file():
    with open("answers.json") as file:
        data = json.load(file)
        return data


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                               5000,
                                                               '/',
                                                               credentials))

channel = connection.channel()


while True:
    method_frame, header_frame, body = channel.basic_get('my_queue')
    if method_frame:
        try:
            data = check_file()
            answer = Answer(data)
            print(method_frame, header_frame, body)
            channel.basic_ack(method_frame.delivery_tag)
        except:
            sleep(1)
    else:
        try:
            answer.process_message()
        except:
            sleep(1)
