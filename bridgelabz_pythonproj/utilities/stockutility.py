import json


class Stocks:
    def __init__(self):
        pass

    def sell(self):
        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
            str = f.read()
            o = json.loads(str)
        name = input("confirm name ")
        b = int(input("how many you want to sell "))
        for p in o['details']:
            if p['name'] == name:
                p['shares'] = int(p['shares']) - b
                p['amount'] = p['amount'] + (1000*b)
                #self.account_details(name)

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:

            f.write(json.dumps(o, indent=2))
            f.close()

    def buy(self):
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'r') as f:
            s = f.read()
            obj = json.loads(s)
            print(" name     number of share     price")
            for n in obj['Stock Report']:
                print(n['Stock Name'], " ", n['Number of Share'], " ", n['Share Price'])
        sname = input("enter stock name ")
        for n in obj['Stock Report']:
            if n['Stock Name'] == sname:
                no = int(input("how many "))
                total = int(n['Share Price']) * no
                print("total cost ", total)
                n['Number of Share'] = int(n['Number of Share']) - no
                with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'w') as f:
                    f.write(json.dumps(obj, indent=2))
                    f.close()
                with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
                    str = f.read()
                    o = json.loads(str)
                name = input("confirm name ")
                for p in o['details']:
                    if p['name'] == name:
                        p['amount'] = int(p['amount']) - total
                        if p['amount'] <= 0:
                            print("error")
                            break

                with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:

                    f.write(json.dumps(o, indent=2))
                    f.close()

    def add(self):
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'r') as f:
            str = f.read()
            obj = json.loads(str)
        stock_name = input("enter stock name ")
        no_share = input("number of shares ")
        price = input("price ")
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'w') as f:
            obj['Stock Report'].append({
                "Stock Name": stock_name,
                "Number of Share": no_share,
                "Share Price": price
            })
            f.write(json.dumps(obj, indent=2))
            f.close()

    def create_account(self):
        print("*********************create account***********************")
        name = input("enter name ")
        self.amount = input("enter amount ")
        shares = int(input("shares "))

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
            str = f.read()
            obj = json.loads(str)

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:
            obj['details'].append({
                "name": name,
                "amount": self.amount,
                "shares": shares,

            })
            f.write(json.dumps(obj, indent=2))
            f.close()
        self.account_details(name)

    def account_details(self, name):

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', ) as f:
            data = json.load(f)
        for r in data["details"]:
            if r['name'] == name:
                print("***************************hello***************************")
                print(r['name'], r['amount'], r['shares'])
        else:
            print("not found")
            exit()

s = Stocks()
