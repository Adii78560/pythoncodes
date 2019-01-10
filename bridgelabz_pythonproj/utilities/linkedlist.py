class Node:
    def __init__(self, data=None):
        self.data = data  # data node
        self.next = None  # last element of list initialise to none as it is always store null value.
        self.next_node = next

    def get_data(self):  # get data of node
        return self.data

    def get_next(self):  # get next node
        return self.next

    def set_next(self, new_next):  # sets the next element to  next node.
        self.next = new_next


class LinkedList:  # wrapper class for node class
    def __init__(self):
        self.head = Node()
        # allow us to point to first node.

    def add(self, data):  # appends  element to list
        new_node = Node(data)  # creates a new node using class node .
        current = self.head  # point to first node
        while current.next is not None:  # while next element  is not Null
            current = current.next  # set the current node to next node
        current.next = new_node  # create the new node after current

    def length(self):  # calculates length of list
        current = self.head
        total = 0

        while current:  # for current node
            total += 1  # incrementing total.
            current = current.get_next()
        return total

    def display(self):  # to display list

        elements = []  # create empty list to display
        current_node = self.head  # Set current node to head
        while current_node.next is not None:
            current_node = current_node.next  # sore next to current
            elements.append(current_node.data)  # Appending to elements list

        return elements


my_list = LinkedList()
