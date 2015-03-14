from ..decorators import json
from ..models import model_v1
from . import api
from flask import Response

@api.route('/names/', methods=['GET'])
@json
def get_names():
    return {'names': 'hello world'}

@api.route('/test/', methods=['GET'])
@json
def test_404():
    resp
