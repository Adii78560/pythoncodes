'''
/**********************************************************************************
* Purpose: stock management queue
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 8-1-2019
*
***********************************************************************************/
'''

from utilities import stockutilqueue


def stock():
    print("1. login / 2. create account")  # ask user whether he/she want to login or create account
    i = int(input())
    if i == 1:
        name = input("enter name ")
        stockutilqueue.ss.account_details(name)
    else:
        stockutilqueue.ss.create_account()

    print("enter choice 1.sell 2.buy 3.add ")  # after login ask for sell/buy/add share
    ch = int(input())
    try:
        if ch == 1:
            stockutilqueue.ss.sell()
        elif ch == 2:
            stockutilqueue.ss.buy()
        elif ch == 3:
            stockutilqueue.ss.add()
        else:
            print("wrong choice")
            raise ValueError
    except ValueError:
        print("only int")

if __name__ == "__main__":
    stock()