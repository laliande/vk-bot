from flask import Blueprint
from flask import request
from json import dumps, dump
from responses import bad_data, bad_mimetype, good_data
from validation import ValidationForMessages, ValidationForGroup

api = Blueprint('api', __name__)


@api.route('/sendDataAboutGroup', methods=['POST'])
def get_data_about_group():
    data = request.get_json()
    try:
        ValidationForGroup
        with open('about_group.json', 'w') as f:
            dump(data, f)
        return good_data
    except:
        return bad_mimetype


@api.route('/sendDataAboutMessages', methods=['POST'])
def get_data_about_messages():
    data = request.get_json()
    try:
        ValidationForMessages(data)
        with open('about_bot.json', 'w') as f:
            dump(data, f)
        return good_data
    except:
        return bad_mimetype
