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


# with open("/home/admin1/BridgeLabz_Python/demo.json", ) as f:
#     data = json.load(f)  # type is dict     # json string to python object(dict and list)
#     # loads() method loads a string s stands for string
#     print(data)


def order():
    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', ) as f:
        data = json.load(f)   # load data from json file

        print("Available items in our grocery store:")
        # show = json.dumps(data, indent=2)
    print("rice :")
    for r in data["rice"]:
        print(r['name'], " Per kg", r['price'], "Available", r['available'], "kg")

    print("Pulses :")
    for p in data['pulses']:
        print(p['name'], " Per kg", p['price'], "Available", p['available'], "kg")

    print("Wheats :")
    for w in data['wheat']:
        print(w['name'], " Per kg", w['price'], "Available", w['available'], "kg")

    print("what to add:")

    i = input("rice or pulse or wheat")
    item_name = input("item name")
    price = int(input("price"))
    quantity = int(input("quantity"))

    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', 'r') as f:
        str = f.read()
        obj = json.loads(str)

    with open('/home/admin1/bridgelabz_pythonproj/samplejson.json', 'w') as f:
        obj[i].append({
            "name": item_name,
            "price": price,
            "available": quantity
        })
        f.write(json.dumps(obj, indent=2))
        f.close()

order()

