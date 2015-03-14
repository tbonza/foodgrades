from ..decorators import json, bad_json
from ..models import model_v1
from . import api
from flask import abort

@api.route('/restaurants/', methods=['GET'])
@json
def get_all_restaurants():
    restaurants = model_v1()
    if not restaurants:
        abort(404)
    return restaurants

@api.route('/restaurants/name/<restaurant_name>', methods=['GET'])
def get_restaurant_name(restaurant_name):
    """ http://stackoverflow.com/questions/12435297 """
    import json
    restaurants = model_v1()

    if not restaurants:
        abort(404)
    else:
       result = [restaurants[key] 
                for key in restaurants
                if restaurant_name.lower() \
                 in restaurants[key]["BusinessName"].lower()]
    return json.dumps(result)



@api.route('/hmm/<articleid>', methods=['GET'])
@json
def get_hmm(articleid):
    restaurants = model_v1()
    namefound = {}
    for key in restaurants:
        if articleid.lower() in restaurants[key]['BusinessName'].lower():
            namefound[restaurants[key]['BusinessName']] \
                = restaurants[key]
    return namefound

    
    return {'you are reading ' + articleid: 'true'}
    

@api.route('/names/', methods=['GET'])
@json
def get_names():
    return {'names': 'hello world'}

@api.route('/test/', methods=['GET'])
@json
def get_missing():
    
    return abort(404)
