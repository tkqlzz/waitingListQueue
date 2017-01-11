class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        newNode = Node(data)
        self.length += 1
        if self.rear == None:
            self.rear = newNode
            self.front = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.front == None:
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.length -= 1
            return data