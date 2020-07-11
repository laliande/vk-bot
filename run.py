from vk import Answer
import os.path
import json

def check_file():
    path = 'answers.json'
    while True:
        if os.path.exists(path):
            with open("answers.json") as file:
                data = json.load(file)
                return data


data = check_file()
answer = Answer(data)
answer.process_message()
        
