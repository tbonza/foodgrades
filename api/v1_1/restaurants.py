from ..decorators import json
from ..models import model_v1
from . import api_1_1
from flask import abort

@api_1_1.route('/restaurants/name/<restaurant_name>', methods=['GET'])
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
