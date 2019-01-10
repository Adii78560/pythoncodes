import json


from utilities.linkedlist import LinkedList

ll = LinkedList()   # object of linked list
with open("/home/admin1/bridgelabz_pythonproj/stockl.json", "r") as sf:
    stock = json.load(sf)        # json obj to python obj i.e. dict

for i in stock['Stock Report']:
    ll.add(i)                      # add and display linked list
print(ll.display())
print(ll.length())

name = input("name")
number = int(input("no"))
price = int(input("price"))

add = {                     # format of data to be enter in file
      "Stock Name": name,
      "Number of Share": number,
      "Share Price": price
}

ll.add(add)
print(ll.length())
print(ll.display())

add_stock = {"Stock Report": []}   # empty dictionary
for item in ll.display():
    add_stock["Stock Report"].append(item)        # append items to dict

with open("/home/admin1/bridgelabz_pythonproj/stockl.json", "w") as f:
    data = json.dumps(add_stock, indent=2)    # python string obj to json
    f.write(data)
print(data)