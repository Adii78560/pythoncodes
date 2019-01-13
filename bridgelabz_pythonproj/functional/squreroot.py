'''
/**********************************************************************************
* Purpose: Write a static function sqrt to compute the square root of a
* nonnegative number
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


def sqr():
    u = Util()

    c = int(input("take a number of which sqrt is to be calculate: "))

    u.sqr_num(c)


if __name__ == "__main__":
    sqr()
