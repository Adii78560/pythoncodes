'''
/**********************************************************************************
* Purpose: Computes the prime factorization of N.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def primen():
    u = Util()

    num = int(input("enter number for factorization: "))

    u.prime(num)


if __name__ == "__main__":
    primen()
