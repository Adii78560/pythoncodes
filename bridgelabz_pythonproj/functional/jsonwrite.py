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


inventory = """                        
{
    "rice": [
                {
                    "name" : "basmati",
                    "price" : 100,
                    "weight" : 200,
                    "available" : 200
                                        


                },
                {
                    "name" : "kolam",
                    "price" : 70,
                    "weight" : 220,
                    "available" : 220

                }
            ],
    "pulses": [
                {
                    "name" : "dry beans",
                    "price" : 140,
                    "weight" : 200,
                    "available" : 200
                },
                {
                    "name" : "dry peas",
                    "price" : 103,
                    "weight" : 250,
                    "available" : 250
                }
               ],
    "wheat":  [
                {
                    "name" : "emmer",
                    "price" : 200,
                    "weight" : 250,
                    "available" : 250
                },

                {
                    "name" : "spelt",
                    "price" : 100,
                    "weight" : 150,
                    "available" : 150
                }
                ]
}

"""

data = json.loads(inventory)  # take data from data using loads i.e. load string
print(type(data))  # type of data variable
print(data)


def inventorym():
    for inventory in data['rice']:  # from inventory take names of rice
        print(inventory['name'])

    with open('../samplejson.json', 'w') as outfile:  # stores data in json file
        json.dump(data, outfile, indent=2)  # indent for cascade format which add spaces

    with open('../samplejson.json', 'r') as f:  # read file
        new = json.load(f)  # load data from file
    for w in new['wheat']:  # take only names and price for wheat
        wn = w['name']
        wp = w['price']
        print(wn, wp)

    print(len(data['rice']))  # total rice entity
    print(len(data))  # total entities in inventory
    l = []  # for all
    r = []  # for rice
    w = []  # for wheat
    p = []  # for pulses
    for i in new['rice']:
        l.append(i['price'])
        r.append(i['price'])
    print("rice ", sum(r))
    for i in new['wheat']:
        l.append(i['price'])
        w.append(i['price'])
    print("wheat ", sum(w))
    for i in new['pulses']:
        l.append(i['price'])
        p.append(i['price'])
    print("pulses ", sum(p))
    print("sum ", sum(l))


inventorym()
