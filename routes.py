from flask import Blueprint
from flask import request
from responses import good_data
import json
api = Blueprint('api', __name__)



@api.route('/send', methods=['POST'])
def send():
    new_data = request.get_json()
    with open("answers.json", "w") as answers:
            json.dump(new_data, answers)
    return good_data


