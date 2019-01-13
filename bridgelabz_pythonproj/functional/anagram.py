'''
/**********************************************************************************
* Purpose: One string is an anagram of another if the second is simply a
* rearrangement of the first.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 26-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def ana():
    u = Util()

    str1 = input("enter string 1: ")
    str2 = input("enter string 2: ")
    u.anagram_check(str1, str2)


if __name__ == "__main__":
    ana()








