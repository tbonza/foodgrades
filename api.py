from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# Read in restaurant info

ID = 1 # id is in 2nd column of restaurant data
restaurants = {} # dict of restaurants ("id" -> dict of restaurant data)

with open('grades.txt') as file:
    fields = file.readline().rstrip('\n\r').split('\t') # strings of restaurant data fields 
    for line in file:
        restaurant = line.split('\t') # list of restaurant values
        restaurants[restaurant[ID]] = {}
        for i, field in enumerate(fields):
            restaurants[restaurant[ID]][field] = restaurant[i]

def abort_if_restaurant_doesnt_exist(restaurant_id):
    if restaurant_id not in restaurants:
        abort(404, message="Restaurant {} doesn't exist".format(restaurant_id))

class Restaurant(Resource):
    def get(self, restaurant_id):
        abort_if_restaurant_doesnt_exist(restaurant_id)
        return restaurants[restaurant_id]

api.add_resource(Restaurant, '/restaurants/<restaurant_id>')

if __name__ == '__main__':
    app.run(debug=True)
