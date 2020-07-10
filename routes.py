from flask import Blueprint
from flask import request
from responses import good_data
from tasks import connect_run
from redis import Redis
from rq import Queue
from vk import Answer

api = Blueprint('api', __name__)

q = Queue(connection=Redis())

@api.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    q.enqueue(connect_run, data)
    return good_data
