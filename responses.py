from flask import Response
from json import dumps


class Responses(Response):
    default_mimetype = 'application/json'


bad_mimetype = Responses(dumps({'Response': 'bad mimetype'}), status=404)
bad_data = Responses(
    dumps({'Response': 'not a valid format data'}), status=404)
good_data = Responses(dumps({'Response': 'ok'}))
