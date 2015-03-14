from ..decorators import json
from ..models import model_v1
from . import api
from flask import abort, jsonify

@api.route('/restaurants/', methods=['GET'])
@json
def get_all_restaurants():
    restaurants = model_v1()
    if not restaurants:
        abort(404)
    return restaurants

@api.route('/restaurants/name/<restaurant_name>', methods=['GET'])
@json
def get_restaurant_name(restaurant_name):
    restaurants = model_v1()
    restaurantsWithName = []
    for key in restaurants:
        if restaurants[key]["BusinessName"] == restaurant_name:
            restaurantsWithName.append(restaurants[key])
    return restaurantsWithName

@api.route('/hmm/<articleid>', methods=['GET'])
#@json
def get_hmm(articleid):
    return 'you are reading ' + articleid
    




@api.route('/names/', methods=['GET'])
@json
def get_names():
    return {'names': 'hello world'}

@api.route('/test/', methods=['GET'])
@json
def get_missing():
    
    return abort(404)
