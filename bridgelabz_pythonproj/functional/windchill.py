'''
/**********************************************************************************
* Purpose: Write a program WindChill.java that takes two double command­line arguments t
* and v and prints the wind chill.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 24-12-2018
*
***********************************************************************************/
'''

from utilities.utility import Util


def wind():
    u = Util()

    t = int(input("enter value for t: "))
    v = int(input("enter value for v: "))

    u.win(t, v)


if __name__ == "__main__":
    wind()
