from ..decorators import json
from ..models import model_v1
from . import api_1_0
from flask import abort

@api_1_0.route('/restaurants/', methods=['GET'])
@json
def get_all_restaurants():
    restaurants = model_v1()
    if not restaurants:
        abort(404)
    return restaurants

@api_1_0.route('/restaurants/name/<restaurant_name>', methods=['GET'])
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

@api_1_0.route('/restaurants/zip/<restaurant_zip>', methods=['GET'])
def get_restaurants_zip(restaurant_zip):
    """ Search for restaurant using zip code """
    import json
    restaurants = model_v1()

    if not restaurants:
        abort(404)
    else:
        results = [restaurants[key]
                   for key in restaurants
                   if restaurant_zip == restaurants[key]["ZIP"]]
    return json.dumps(results)

@api_1_0.route('/restaurants/id/<restaurant_id>', methods=['GET'])
@json
def get_restaurants_id(restaurant_id):

    restaurants = model_v1()

    if not restaurants:
        abort(404)
    if restaurant_id not in restaurants:
        abort(404)
    return restaurants[restaurant_id]
