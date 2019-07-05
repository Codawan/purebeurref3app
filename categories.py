import requests

from constants import CATEGORIES_NEEDED

try:
    cat_response = requests.get('https://world.openfoodfacts.org/categories.json')
    print(cat_response)
except:
    print("Can't connect to the API")

data = cat_response.json()
category_list = data['tags']

# Let's make a dictionary of a limited number of categories

categories = {}

for category in range(0, CATEGORIES_NEEDED):  
    categories[category_list[category].get('name')] = category_list[category].get('url') + "/1.json"

print(categories)