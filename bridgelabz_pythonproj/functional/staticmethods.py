'''
/**********************************************************************************
* Purpose: Create Utility Class having following static methods
* i.binarySearch method for integer
* ii.binarySearch method for String
* iii.insertionSort method for integer
* iv.insertionSort method for String
* v.bubbleSort method for integer
* vi.bubbleSort method for String

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util

list_string = ["janhavi", "rohini", "nikhil", "pushkar", "abhishek", "gautami"]
list_int = [7, 3, 5, 2, 1]


def method():
    u = Util()
    key = int(input("enter number to be search: "))
    u.binarysearchint(list_int, key)

    key2 = input("enter string to be search: ")
    u.binarysearchstring(list_string, key2)

    u.bubblesortint(list_int)
    u.bubblesortstring(list_string)
    u.insertionsortint(list_int)
    u.insertionsortstring(list_string)


if __name__ == "__main__":
    method()
