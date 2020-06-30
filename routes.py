from flask import Blueprint
from flask import request
from flask import Response
from json import dumps, dump

api = Blueprint('api', __name__)


@api.route('/getDataAboutGroup', methods=['POST'])
def getDataAboutGroup():
    data = request.get_json()
    if data is None:
        return Response(dumps({'Response': 'no valid mimetype data'}), status=404, mimetype='application/json')
    else:
        try:
            about_group = {'token': data['token'], 'group_id': data['group_id'],
                           'version_api': data['version_api']}

            with open('data.json', 'w') as f:
                dump(about_group, f)

            return Response(dumps({'Response': 'ok'}), status=200, mimetype='application/json')
        except:
            return Response(dumps({'Response': 'no valid format data'}), status=404, mimetype='application/json')
