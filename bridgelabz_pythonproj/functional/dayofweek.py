'''
/**********************************************************************************
* Purpose: To the Util Class add dayOfWeek static function that takes a date as input and
* prints the day of the week that date falls on.
* logic :
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 26-12-2018
*
***********************************************************************************/
'''

from utilities import utility
day = int(input("enter day: "))
if 0 < day < 32:                 # day must be between 1 to 31
    months = int(input("enter month: "))
    if 0 < months < 13:          # month between 1 - 12
        year = input("enter year: ")
        if len(year) == 4:        # length should be 4 for year
            utility.day_week(day, months, year)
        else:
            print("invalid year")
    else:
        print("invalid month")
else:
    print("invalid day")
