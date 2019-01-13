'''
/**********************************************************************************
* Purpose: A library for reading in 2D arrays of integers, doubles, or booleans from
* standard input and printing them out to standard output.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 22-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def arr():
    u = Util()

    n = int(input("enter number of rows: "))  # take number of rows and columns fom user
    m = int(input("enter number of columns: "))

    u.arrays(n, m)


if __name__ == "__main__":
    arr()
