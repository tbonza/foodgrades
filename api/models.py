



def grades_txt(restaurants):
    """ Reads in grades text file, returns dictionary

    args:
        restaurants: dict, empty dictionary

    returns:
        dictionary populated with restaurant grades of the form:
    
        grades_txt(restaurants)['1']
        {'LICENSENO': '34789',
         'count_3': '0',
         'count_2': '0',
         'count_1': '8',
         'City': 'Roxbury',
         'Grade': 'A',
         'LICSTATUS': 'Inactive',
         'ZIP': '02118',
         'State': 'MA',
         'BusinessName': '1000 Washington Cafe',
         'EXPDTTM': '12/31/2011 23:59',
         'ID': '1',
         'Address': '1000 Washington ST'}
    """
    # id is in 2nd column of restaurant data
    id_field = 1
    
    with open('data/grades.txt') as file:
        # strings of restaurant data fields 
        fields = file.readline().rstrip('\n').rstrip('\r').split('\t') 
        for line in file:
            # list of restaurant values
            restaurant = line.rstrip('\n').rstrip('\r').split('\t') 
            restaurants[restaurant[id_field]] = {}
            for i, field in enumerate(fields):
                restaurants[restaurant[id_field]][field] = restaurant[i]
    file.close()
    return restaurants


def violations_txt(restaurants):
    """ Reads in violations.txt, returns dictionary 

    args:
        restaurants: dict, first populated with grades.txt

    returns:
        dictionary populated with violatins info, of the form:

        violations_txt(restaurants)['1']['violations']['1']
        {'LICENSENO': '34789',
         'ISSDTTM': '11/7/2011 8:34',
         'ZIP': '02118',
         'VIOLDTTM': '2/9/2011 11:05',
         'Violation': '21-3-304.14',
         'ViolLevel': '*',
         'Comments': 'Keep wiping cloths in sanitizer',
         'LICSTATUS': 'Inactive',
         'ViolStatus': 'Fail',
         'LICENSECAT': 'FS',
         'City': 'Roxbury',
         'State': 'MA',
         'RESULT': 'HE_Filed',
         'BusinessName': '1000 Washington Cafe',
         'ViolDesc': 'Wiping Cloths  Clean  Sanitize',
         'ViolDate': '02/09/2011',
         'EXPDTTM': '12/31/2011 23:59',
         'ID': '1',
         'Address': '1000   Washington ST'}
    """
    # Read in violations info

    id_field = 0 # id is in the 1st column of the violations data

    with open('data/violations.txt') as file:
        # strings of violation data fields
        fields = file.readline().rstrip('\n').rstrip('\r').split('\t') 
        for line in file:
            # list of violation values
            violation = line.rstrip('\n').rstrip('\r').split('\t') 
            restaurant_id = violation[id_field]
            if not "violations" in restaurants[restaurant_id]:
                restaurants[restaurant_id]["violations"] = {}
                violation_id = 1 # starts at 1 for each restaurant
                
            restaurants[restaurant_id]["violations"]\
                [str(violation_id)] = {}
            
            for i, field in enumerate(fields):
                restaurants[restaurant_id]["violations"]\
                    [str(violation_id)]\
                [field] = violation[i]
        violation_id += 1 
    file.close()
    return restaurants

def model_v1():
    """ Read in restaurant info, return data structure for api v1.0 """

    # dict of restaurants ("id" -> dict of restaurant data)
    restaurants = {} 

    restaurants = grades_txt(restaurants)
            
    restaurants = violations_txt(restaurants)

    return restaurants
