import mysql.connector

from categories import *

import requests

# Connection to the database

pbdb = mysql.connector.connect(
    host='localhost',
    database='purebeurre',
    user='pb_user',
    passwd='PYTHON2019'
)

print(pbdb)

# Api request

response = requests.get(SAUCISSONS)
data = response.json()
products_list = data['products']

for product in products_list:
    print(
        "Nom: " + product.get('product_name_fr'),
        "Code: " + product.get('code'),
        "Description: " + str(product.get('generic_name_fr')),
        "Nutriscore:  " + str(product.get('nutrition_grade_fr')),
        "Où acheter?: " + str(product.get('stores')),
        "Lien OFF: " + product.get('url')
        )
