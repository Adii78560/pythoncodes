'''
this is basic code for creating Node and queue in which nodes stores values. enqueue is used to
add elements. dequeue use to remove element. Size will give size of linked list. show is used to
display linked list
'''


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    front = None
    rear = None

    def __init__(self):

        pass

    def enqueue(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = self.rear.next

    def show(self):

        if self.front == None:
            print("Linked List  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


queue = Queue()


class Stack:  # create stack
    top = 0
    head = None

    def __init__(self):  # constructor for stack
        pass

    def push(self, data):  # enter data in stack

        node = Node(data)

        if self.head == None:

            self.head = node
        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next  # traversing nodes

            traverse.next = node

    def size(self):  # size of stack
        traverse = self.head

        if self.head == None:
            return 0
        size = 1
        while traverse.next != None:
            traverse = traverse.next  # traverse every node and every time increment size
            size += 1
        return size

    def show(self):  # display stack
        traverse = self.head

        if self.top <= -1:  # initially starting node is -1 then stack is underflow
            print(" Stack Underflow")
            return
        if traverse == None:
            print("Stack is empty")  # empty stack
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)

    def pop(self):  # remove from stack

        traverse = self.head

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None

            return traverse.data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None

                return t1.data
            traverse = traverse.next

    def peek(self):  # peeks last entered element of stack as stack works on last in first out
        traverse = self.head

        if self.head == None:
            return "empty stack"
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next

        return traverse.data

    def is_empty(self):  # check whether stack is empty or not

        if self.size() == 0:
            return True
        else:
            return False


stack = Stack()
stack1 = Stack()