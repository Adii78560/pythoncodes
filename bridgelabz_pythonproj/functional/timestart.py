'''
/**********************************************************************************
* Purpose: Write a Stopwatch Program for measuring the time that elapses between
* the start and end clicks
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 24-12-2018
*
***********************************************************************************/
'''


from utilities.utility import Util


def timers():
    u = Util()
    start_value = int(input("enter 1 to start: "))   # to start stopwatch
    u.stopwatch(start_value)


if __name__ == "__main__":
    timers()
