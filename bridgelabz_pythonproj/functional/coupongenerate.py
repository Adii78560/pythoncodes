'''
/**********************************************************************************
* Purpose: Prints the harmonic value: 1/1 + 1/2 + ... + 1/N
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 22-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def cop():
    u = Util()

    coupon_number = int(input("enter coupon number: "))  # take input for coupon number

    u.coupon(coupon_number)


if __name__ == "__main__":
    cop()
