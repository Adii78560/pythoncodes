'''
/**********************************************************************************
* Purpose: Write a program to read in Stock Names, Number of Share, Share Price.
* Print a Stock Report with total value of each Stock and the total value of Stock.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 7-1-2019
*
***********************************************************************************/
'''

import json

stock = """                        
{
    "reliance": [
                {
                    "stock name" : "abc",
                    "number of shares" : 100,
                    "share price" : 200

                },
                {   "stock name" : "cbd",
                    "number of shares" : 10,
                    "share price" : 20

                }
            ],
    "goggle": [
                {
                    "stock name" : "xyz",
                    "number of shares" : 50,
                    "share price" : 10
                },
                {
                    "stock name" : "pqr",
                    "number of shares" : 55,
                    "share price" : 25
                }
               ],
    "hdfc":  [
                {
                    "stock name" : "vpl",
                    "number of shares" : 30,
                    "share price" : 20
                },

                {
                    "stock name" : "lkj",
                    "number of shares" : 100,
                    "share price" : 80
                }
                ]
}

"""
data = json.loads(stock)  # take data from data using loads i.e. load string

# print(data)
with open('/home/admin1/bridgelabz_pythonproj/stock.json', '+w') as outfile:  # stores data in json file
    json.dump(data, outfile, indent=2)  # indent for cascade format which add spaces


def stock():
    with open('/home/admin1/bridgelabz_pythonproj/stock.json', 'r') as f:  # read file
        new = json.load(f)  # load data from file
    l = []
    for w in new["reliance"]:  # take only names and price for wheat
        wn = w['number of shares'] * w['share price']
        l.append(wn)
        print("value of stock of reliance ", wn)
    for w in new["goggle"]:  # take only names and price for wheat
        wn = w['number of shares'] * w['share price']
        l.append(wn)
        print("value of stock of google ", wn)
    for w in new["hdfc"]:  # take only names and price for wheat
        wn = w['number of shares'] * w['share price']
        l.append(wn)
        print("value of stock of hdfc ", wn)
    print(l)
    print("value of total stocks", sum(l))


stock()
