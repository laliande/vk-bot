import threading
from vk import Answer

import time
import random

groups = set()


def worker(data, group_id):
    answer = Answer(data)
    while group_id in groups:
        answer.process_message()


def start(data, group_id, action):
    if action == 'start':
        t = threading.Thread(target=worker, args=(data, group_id))
        groups.add(group_id)
        t.start()
    elif action == 'stop':
        groups.discard(group_id)

    else:
        return "bad action"
