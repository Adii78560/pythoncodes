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

class DeckOfCards:
    def __init__(self):
        pass

    def cards(self):
        suit = ("Clubs", "Diamonds", "Hearts", "Spades")
        rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

        card_list = []

        while len(card_list) < 36:
            for i in range(0, 9):
                random_rank = random.randint(0, 12)
                random_suit = random.randint(0, 3)
                rank_val = rank[random_rank]
                suit_val = suit[random_suit]

                rank_val = rank_val + "-" + suit_val

                if rank_val not in card_list:
                    if len(card_list) is not 36:
                        card_list.append(rank_val)

        row = 4
        column = 9

        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0

        for i in range(row):
            for j in range(column):
                two_d_array[i][j] = card_list[index]
                index += 1

        twod = np.array(two_d_array)

        print(twod)

d = DeckOfCards()
d.cards()



