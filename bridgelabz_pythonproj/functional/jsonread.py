'''
/**********************************************************************************
* Purpose: Create a JSON file having Inventory Details for Rice, Pulses and Wheats
* with properties name, weight, price per kg.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 7-1-2019
*
***********************************************************************************/
'''

import json


def order():
    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', ) as f:
        data = json.load(f)   # load data from json file

        print("Available items in our grocery store:")
        # show = json.dumps(data, indent=2)
    print("rice :")
    for r in data["rice"]:    # get the entities from key rice
        print(r['name'], " Per kg", r['price'], "Available", r['available'], "kg")

    print("Pulses :")        # get the entities
    for p in data['pulses']:
        print(p['name'], " Per kg", p['price'], "Available", p['available'], "kg")

    print("Wheats :")          # get entities
    for w in data['wheat']:
        print(w['name'], " Per kg", w['price'], "Available", w['available'], "kg")

    print("what to add:")

    i = input("rice or pulse or wheat")
    item_name = input("item name")
    price = int(input("price"))
    quantity = int(input("quantity"))

    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', 'r') as f:
        str = f.read()      # open and read file
        obj = json.loads(str)      # read json file like object and parse to string

    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', 'w') as f:
        obj[i].append({               # open file in write mode and append values
            "name": item_name,
            "price": price,
            "available": quantity
        })
        f.write(json.dumps(obj, indent=2))        # json object to string
        f.close()

order()


