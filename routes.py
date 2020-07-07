from flask import Blueprint
from flask import request
from json import dumps, dump
from responses import Responses, bad_data, bad_mimetype, good_data

api = Blueprint('api', __name__)


@api.route('/sendDataAboutGroup', methods=['POST'])
def get_data_about_group():
    data = request.get_json()
    if data is None:
        return bad_mimetype
    else:
        try:
            about_group = {'token': data['token'], 'group_id': data['group_id'],
                           'version_api': data['version_api']}

            with open('data.json', 'w') as f:
                dump(about_group, f)

            return good_data
        except:
            return bad_data


@api.route('/sendDataAboutMessages', methods=['POST'])
def get_data_about_messages():
    pass
