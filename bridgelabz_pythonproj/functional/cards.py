'''
/**********************************************************************************
* Purpose: initialize deck of cards having suit ("Clubs",
* "Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
* "Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then
* distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players
* using 2D Array
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 8-1-2019
*
***********************************************************************************/
'''
import random
import numpy as np


class Card:

    def __init__(self):
        pass

    def selectcard(self):
        card_name = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        list_cards = []

        while len(list_cards) < 36:
            for i in range(0, 9):

                random_int = random.randint(1, 13)

                card_index = rank[random_int - 1]  # length of Rank - 1 i.e store value acco to index

                random_suit = random.randint(0, 3)

                card_index = card_index + '-' + card_name[random_suit]

                if list_cards.__contains__(card_index) is False:

                    if len(list_cards) is not 36:
                        list_cards.append(card_index)

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0

        for i in range(row):
            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1

        twod = np.array(two_d_array)

        return twod


c = Card()
print(c.selectcard())
