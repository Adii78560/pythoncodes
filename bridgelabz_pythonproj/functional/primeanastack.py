'''
/**********************************************************************************
* Purpose: prime numbers which are anagram using stack

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''
from utilities import datastructqueue
from functional import primeanagram
l = primeanagram.c.a_list
for i in l:
    datastructqueue.stack.push(i)  # push ith element to stack
print("\n \n stack ...\n")
for i in range(0, datastructqueue.stack.size()):
    print(datastructqueue.stack.pop(), end=" ")   # print pop elements
