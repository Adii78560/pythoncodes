'''
/**********************************************************************************
* Purpose: Write a Util Static Function to calculate monthlyPayment that reads in three
* command­line arguments P, Y, and R and calculates the monthly payments you
* would have to make over Y years to pay off a P principal loan amount at R per cent
* interest compounded monthly.
* logic :
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 26-12-2018
*
***********************************************************************************/
'''
from utilities.utility import Util


def pay():
    u = Util()
    p = int(input("enter principal loan amount p: "))
    y = int(input("enter years y: "))
    r = int(input("enter rate r: "))

    u.monthly_pay(p, y, r)


if __name__ == "__main__":
    pay()
