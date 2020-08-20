import threading
from concurrent.futures import ProcessPoolExecutor
from vk import Answer

import time
import random

groups = set()
max_workers = 1
num_active_workers = 0


def worker(answer, group_id):
    while group_id in groups:
        answer.process_message()


executor = ProcessPoolExecutor(max_workers=max_workers)


def start(data, group_id, action):
    global max_workers, num_active_workers
    if action == 'start':
        if group_id in groups:
            return 'this group now runing'
        groups.add(group_id)
        try:
            answer = Answer(data)
        except Exception as ex:
            return ex
        if num_active_workers < max_workers:
            new_process = executor.submit(worker, answer, group_id)
            num_active_workers += 1
        else:
            return 'the overflow process pool'
    elif action == 'stop':
        groups.discard(group_id)
        if num_active_workers != 0:
            num_active_workers -= 1
    else:
        return "bad action"
