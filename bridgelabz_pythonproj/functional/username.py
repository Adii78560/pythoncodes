'''
/**********************************************************************************
* Purpose: User Input and Replace String Template “Hello <<UserName>>, How are you?”
* logic:-taking user input for username and replacing
*        <<username>> with user entered username
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities.utility import Util


def user():
    u = Util
    username = input("enter username: ")  # take username from user to replace with <<username>>
    u.username_change(username)


if __name__ == "__main__":
    user()
