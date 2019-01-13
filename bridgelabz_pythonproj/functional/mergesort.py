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

array = [5, 4, 3, 2, 1]


def sorting():
    u = Util()
    print("unsorted: ", array)

    result = u.merge_sort(array)
    print("sorted: ", result)


if __name__ == "__main__":
    sorting()
