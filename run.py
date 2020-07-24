import pika
import pika
from vk import Answer
import json
from time import sleep


def check_file():
    with open("answers.json") as file:
        data = json.load(file)
        return data

while True:
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    method_frame, header_frame, body = channel.basic_get('my_queue')
    if method_frame:
        data = check_file()
        answer = Answer(data)
        print(method_frame, header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        channel.close()
        connection.close()
        try:
            answer.process_message()
            print('try')
        except:
            print('sleep')
            sleep(1)
                                                                                                                                    
