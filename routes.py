from flask import Blueprint
from flask import request
from responses import good_data

from vk import Answer

api = Blueprint('api', __name__)


@api.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    test = Answer(data)
    test.process_message()
