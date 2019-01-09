class Node:
    def __init__(self, data=None):
        self.data = data  # data node
        self.next = None  # last element of list will alwasys has none .
        self.next_node = next

    def get_data(self):  # gets the data of node
        return self.data

    def get_next(self):  # gets next node
        return self.next

    def set_next(self, new_next):  # used while deleting: sets the next element to other next node.
        self.next = new_next


class LinkedList:  # wrapper class for node class. user will never interface with node
    def __init__(self):
        self.head = Node()  # never gonna contain any actual data.  simply used as placeholder to
        # allow us to point to first node.

    def add(self, data):  # appends  element to list
        new_node = Node(data)  # creates a new node using class node .
        current = self.head  # point to start iteration from ... first node
        while current.next is not None:  # while next element  is not Null
            current = current.next  # sets the current node to next node
        current.next = new_node  # create  the new node after current node

    def length(self):  # calculates length of list
        current = self.head  # at start nodes starts from Head
        total = 0  # variable to count the nodes.

        while current:  # while current = True
            total += 1  # incrementing total.
            current = current.get_next()  # current element = next element until loop finishes
        return total

    def display(self):  # to display list

        elements = []  # list for display
        current_node = self.head  # Set current node to starting node. i.e. HEAD
        while current_node.next is not None:  # Traversing to last node i.e. till end(None)
            current_node = current_node.next
            elements.append(current_node.data)  # Appending to elements list
        # print('data in linked list ', elements)
        return elements


my_list = LinkedList()
