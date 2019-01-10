import json
import datetime
from utilities import datastructqueue


class Stocks:
    def __init__(self):  # constructor for stocks
        pass

    def sell(self):  # sell method
        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
            strr = f.read()  # read file and store in variable
            o = json.loads(strr)  # read file like object and convert to string dict
        name = input("confirm name ")  # username
        sname = input("which share ")
        self.b = int(input("how many you want to sell "))
        for p in o['details']:
            if p['name'] == name:
                p['shares'] = int(p['shares']) - self.b  # subtract sold shares from original value
                p['amount'] = p['amount'] + (1000 * self.b)  # calculate amount of sold shares
                # self.account_details(name)

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:

            f.write(json.dumps(o, indent=2))  # write data in string format to the file
            f.close()

        date_timee = datetime.datetime.today()  # current date time

        # enter data to queue
        datastructqueue.queue.enqueue("\n" + "sell " + sname + " " + str(date_timee))

        with open("/home/admin1/bridgelabz_pythonproj/stockqueue.txt", "a") as file:
            file.write("\n" + "sell " + sname + " " + str(date_timee))

    def buy(self):  # buy shares
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'r') as f:
            s = f.read()
            obj = json.loads(s)
            print(" name     number of share     price")

            for n in obj['Stock Report']:  # display details
                print(n['Stock Name'], " ", n['Number of Share'], " ", n['Share Price'])
        sname = input("enter stock name ")
        for n in obj['Stock Report']:  # if the stock name is there in stock record then proceed
            if n['Stock Name'] == sname:
                self.no = int(input("how many "))
                total = int(n['Share Price']) * self.no  # total cost
                print("total cost ", total)
                n['Number of Share'] = int(n['Number of Share']) - self.no  # update remaining shares
                with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'w') as f:
                    f.write(json.dumps(obj, indent=2))
                    f.close()
                with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
                    strr = f.read()
                    o = json.loads(strr)  # update the amount in users account
                name = input("confirm name ")

                for p in o['details']:
                    if p['name'] == name:
                        p['amount'] = int(p['amount']) - total


                with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:

                    f.write(json.dumps(o, indent=2))
                    f.close()

        date_time = datetime.datetime.today()

        datastructqueue.queue.enqueue("\n"+"buy " + sname + " " + str(self.no) + " " + str(date_time))

        with open("/home/admin1/bridgelabz_pythonproj/stockqueue.txt", "a") as file:
            file.write("buy " + sname + " " + str(self.no) + " " + str(date_time))

    def add(self):  # add new share
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'r') as f:
            strr = f.read()
            obj = json.loads(strr)

        stock_name = input("enter stock name ")
        no_share = input("number of shares ")
        price = input("price ")
        with open('/home/admin1/bridgelabz_pythonproj/stockmanage.json', 'w') as f:
            obj['Stock Report'].append({  # append details
                "Stock Name": stock_name,
                "Number of Share": no_share,
                "Share Price": price
            })
            f.write(json.dumps(obj, indent=2))
            f.close()

    def create_account(self):  # creating users account
        print("*********************create account***********************")
        name = input("enter name ")
        self.amount = input("enter amount ")
        shares = int(input("shares "))

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'r') as f:
            strr = f.read()
            obj = json.loads(strr)

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', 'w') as f:
            obj['details'].append({
                "name": name,
                "amount": self.amount,
                "shares": shares,

            })
            f.write(json.dumps(obj, indent=2))
            f.close()  # close file after modification so that data will not get altered by other operations
        self.account_details(name)

    def account_details(self, name):  # display account details

        with open('/home/admin1/bridgelabz_pythonproj/persondetail.json', ) as f:
            data = json.load(f)
        for r in data["details"]:
            if r['name'] == name:  # fetch data by fetching name attribute
                print("***************************hello***************************")
                print(r['name'], r['amount'], r['shares'])


ss = Stocks()
