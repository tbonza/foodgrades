from ..decorators import json
from . import api

@api.route('/names/', methods=['GET'])
@json
def get_names():
    return {'names': 'hello world'}
