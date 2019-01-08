'''
/**********************************************************************************
* Purpose: stock management
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 8-1-2019
*
***********************************************************************************/
'''

from utilities import stockutility

print("1. login / 2. create account")
i = int(input())
if i == 1:
    name = input("enter name ")
    stockutility.s.account_details(name)
else:
    stockutility.s.create_account()

print("enter choice 1.sell 2.buy 3.add ")
ch = int(input())
if ch == 1:
    stockutility.s.sell()
elif ch == 2:
    stockutility.s.buy()
elif ch == 3:
    stockutility.s.add()
else:
    print("wrong choice")
