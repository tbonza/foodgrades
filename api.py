from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# Read in restaurant info

id_field = 1 # id is in 2nd column of restaurant data
restaurants = {} # dict of restaurants ("id" -> dict of restaurant data)

with open('grades.txt') as file:
    fields = file.readline().rstrip('\n\r').split('\t') # strings of restaurant data fields 
    for line in file:
        restaurant = line.split('\t') # list of restaurant values
        restaurants[restaurant[id_field]] = {}
        for i, field in enumerate(fields):
            restaurants[restaurant[id_field]][field] = restaurant[i]
file.close()

# Read in violations info

id_field = 0 # id is in the 1st column of the violations data

with open('violations.txt') as file:
    fields = file.readline().rstrip('\n\r').split('\t') # strings of violation data fields
    for line in file:
        violation = line.split('\t') # list of violation values
        restaurant_id = violation[id_field]
        if not "violations" in restaurants[restaurant_id]:
            restaurants[restaurant_id]["violations"] = {}
            violation_id = 1 # starts at 1 for each restaurant
        restaurants[restaurant_id]["violations"][str(violation_id)] = {}
        for i, field in enumerate(fields):
            restaurants[restaurant_id]["violations"][str(violation_id)][field] = violation[i]
        violation_id += 1 
file.close()

class Restaurants(Resource):

    def get(self):
        if not restaurants:
            abort(404, message="No Restaurants")
        return restaurants

class Restaurant(Resource):

    def get(self, restaurant_id):
        if restaurant_id not in restaurants:
            abort(404, message="Restaurant {}, doesn't exist".format(restaurant_id))
        return restaurants[restaurant_id]

class Violation(Resource):

    def get(self, restaurant_id, violation_id):
        if violation_id not in restaurants[restaurant_id]["violations"]:
            abort(404, message="Resturant {}, Violation {}, doesn't exist".format(restaurant_id, violation_id))    
        return restaurants[restaurant_id]["violations"][violation_id]

api.add_resource(Restaurants, '/restaurants')
api.add_resource(Restaurant, '/restaurants/<restaurant_id>')
api.add_resource(Violation, '/restaurants/<restaurant_id>/violations/<violation_id>')

if __name__ == '__main__':
    app.run(debug=True)
