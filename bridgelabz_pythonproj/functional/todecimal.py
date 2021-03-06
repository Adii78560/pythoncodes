'''
/**********************************************************************************
* Purpose: Write Binary.java to read an integer as an Input, convert to Binary using toBinary
* function and perform the following functions.
* i. Swap nibbles and find the new number.
* ii. Find the resultant number is the number is a power of 2.
* logic :
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 27-12-2018
*
***********************************************************************************/
'''
from utilities.utility import Util


def decm():
    u = Util()
    m = int(input("enter the number to see its binary representation: "))

    u.decimal_convert(m)


if __name__ == "__main__":
    decm()
