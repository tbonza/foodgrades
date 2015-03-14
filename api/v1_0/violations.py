from ..decorators import json
from ..models import model_v1
from . import api_1_0
from flask import abort

@api_1_0.route('/restaurants/id/<restaurant_id>/violations',
               methods=['GET'])
@json
def get_violations_by_restaurant_id(restaurant_id):
    restaurants = model_v1()

    if not restaurants:
        abort(404)
    if restaurant_id not in restaurants:
        abort(404)
    return restaurants[restaurant_id]["violations"]

@api_1_0.route('/restaurants/id/<restaurant_id>/violations' +\
               '/id/<violation_id>', methods=['GET'])
@json
def get_violations_restaurant_violation_id(restaurant_id, violation_id):
    restaurants = model_v1()

    if not restaurants:
        abort(404)
    if violation_id not in restaurants[restaurant_id]["violations"]:
        abort(404)    
    return restaurants[restaurant_id]["violations"][violation_id]


            
