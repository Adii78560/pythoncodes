import json


from utilities.linkedlist import LinkedList

ll = LinkedList()
with open("/home/admin1/bridgelabz_pythonproj/stockl.json", "r") as sf:
    stock = json.load(sf)

for i in stock['Stock Report']:
    ll.add(i)
print(ll.display())
print(ll.length())

name = input("name")
number = int(input("no"))
price = int(input("price"))

add = {
      "Stock Name": name,
      "Number of Share": number,
      "Share Price": price
}

ll.add(add)
print(ll.length())
print(ll.display())

add_stock = {"Stock Report": []}
for item in ll.display():
    add_stock["Stock Report"].append(item)

with open("/home/admin1/bridgelabz_pythonproj/stockl.json", "w") as f:
    data = json.dumps(add_stock, indent=2)
    f.write(data)
print(data)