# Read in restaurant information from file

ID = 1 # id is in 2nd column of restaurant data

restaurants = {} # dict of restaurants ("id" -> dict of restaurant data)

with open('grades.txt') as file:
    fields = file.readline().rstrip('\n\r').split('\t') # strings of restaurant data fields 
    for line in file:
        restaurant = line.split('\t') # list of restaurant values
        restaurants[restaurant[ID]] = {}
        for i, field in enumerate(fields):
            restaurants[restaurant[ID]][field] = restaurant[i]
