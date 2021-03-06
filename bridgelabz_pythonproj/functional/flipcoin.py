'''
/**********************************************************************************
* Purpose: Flip Coin and print percentage of Heads and Tails
* logic : take user input for how many times user want to flip coin and generate head or
* tail randomly and then calculate percentage for head and tail
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities.utility import Util


def coin():
    u = Util
    n = int(input("number of times to flip coin: "))  # number of times user want to flip coin
    u.flips(n)


if __name__ == "__main__":
    coin()
