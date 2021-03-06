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


def power():
    u = Util()
    n = int(input("enter number of questions: "))

    k = (2**n)-1
    print("think of a integer between 0 to ",k)

    u.guess(0,k)


if __name__ == "__main__":
    power()
