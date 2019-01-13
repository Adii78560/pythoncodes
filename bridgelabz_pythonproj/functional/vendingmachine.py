'''
/**********************************************************************************
* Purpose: Vending machine problem
* logic : Check the list elements and compare the given user amount.
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 27-12-2018
*
***********************************************************************************/
'''
from utilities.utility import Util


def vending():
    u = Util()
    amount = int(input("enter amount: "))   # ask user to enter amount
    u.vending(amount)


if __name__ == "__main__":
    vending()
