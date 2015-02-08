from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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

parser = reqparse.RequestParser()
parser.add_argument('restaurant_name')

class Restaurant(Resource):
    def get(self, restaurant_id):
        abort_if_restaurant_doesnt_exist(restaurant_id)
        return restaurants[restaurant_id]

    def delete(self, restaurant_id):
        abort_if_restaurant_doesnt_exist(restaurant_id)
        del restaurants[restaurant_id]
        return '', 204

    def put(self, restaurant_id):
        args = parser.parse_args()
        restaurants[restaurant_id] = {'restaurant_name': args['restaurant_name']}  
        return restaurants[restaurant_id], 201

api.add_resource(Restaurant, '/restaurants/<restaurant_id>')

if __name__ == '__main__':
    app.run(debug=True)
