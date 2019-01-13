'''
/**********************************************************************************
* Purpose: Write static functions to return all permutation of a String
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 24-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def permutation():
    u = Util()
    data = input("enter string: ")    # enter string for permutation
    print(u.permutation_py(data))


if __name__ == "__main__":
    permutation()

