'''
/**********************************************************************************
* Purpose: Deck of cards extend

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 10-1-2019
*
***********************************************************************************/
'''

import random
import numpy as np
from utilities import datastructqueue


class DeckOfCards:
    """This class is used to write logic for deck of cards"""

    def shuffle(self):

        """Method to distribute 9 cards to 4 users"""

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11 Jack", "12 Queen", "13 King", "14 Ace"]

        list_cards = []  # list to hold cards.

        while len(list_cards) < 36:  # loop will run till 36 because we want to distribute 36 cards to 4 players.
            for i in range(0, 9):  # used to get only  9 numbers

                random_no = random.randint(1, 13)  # generate random number within 1 and 13

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)  # generates random number for suits.
                cards_rank = cards_rank + ' ' + suits[random_no_suits]  # adds suit and Rank together.

                if cards_rank not in list_cards:  # if list of cards does not contains cards_rank already:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)  # append cards_rank to list of cards

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # list comprehensions for matrix.
        index = 0
        for i in range(row):  # row iteration

            for j in range(column):  # column iteration .
                two_d_array[i][j] = list_cards[index]
                index += 1
        # print(two_d_array)
        a = np.array(two_d_array)
        print(a)
        # print("list of cards , : ",list_cards)
        limit = 9
        l1 = []  # four lists are used  for slicing of 36  elements in 4 parts(9 each).
        l2 = []
        l3 = []
        l4 = []

        for i in list_cards[0:9]:
            i = tuple((int(i[:2]), i[2:]))  # because we are getting data like ['12 Queen Spades']. all in string
            # format so we split first two chars converts it to int and  add in tuple which makes to separate
            # elements in one small tuple.
            # also it makes the sorting easy  with Int.

            l1.append(i)  # appends data to list.

        l1.sort()  # sorts the data.
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in l1:
            q1.enqueue(j)  # adds data of player 1 to queue 1.


        q1.show()
        print()

        for i in list_cards[9:18]:
            i = tuple((int(i[:2]), i[2:]))
            l2.append(i)
        l2.sort()
        print("Player 2 Cards")
        for l in l2:
            q2.enqueue(l)  # adds data of player 2 to queue 2.
        q2.show()
        print()

        for i in list_cards[18:27]:
            i = tuple((int(i[:2]), i[2:]))
            l3.append(i)
        l3.sort()
        print("Player 3 Cards")
        for m in l3:
            q3.enqueue(m)  # adds data of player 3 to queue 3.
        q3.show()
        print()

        for i in list_cards[27:]:
            i = tuple((int(i[:2]), i[2:]))
            l4.append(i)

        l4.sort()
        print("Player 4 Cards")
        for n in l4:
            q4.enqueue(n)  # adds data of player 4 to queue 4.
        q4.show()
        return list_cards, two_d_array


q1 = datastructqueue.Queue()  # Queue class objects.
q2 = datastructqueue.Queue()
q3 = datastructqueue.Queue()
q4 = datastructqueue.Queue()

card = DeckOfCards()
card.shuffle()
