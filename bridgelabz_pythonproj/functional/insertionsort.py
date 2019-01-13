'''
/**********************************************************************************
* Purpose: Prints the harmonic value: 1/1 + 1/2 + ... + 1/N
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def sorting():
    u = Util()
    try:
        stringlist = list(input("enter elements for list(only string): ").split(" "))
        u.userstring(stringlist)
    except ValueError:
        print("only strings")


if __name__ == "__main__":
    sorting()



