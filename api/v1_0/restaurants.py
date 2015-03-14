from ..decorators import json
from ..models import model_v1
from . import api

@api.route('/names/', methods=['GET'])
@json
def get_names():
    return {'names': 'hello world'}
