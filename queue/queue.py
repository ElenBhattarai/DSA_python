class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    #enqueue
    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
    
    #dequeue
    def dequeue(self):
        if self.front == None:
            return RuntimeError("Empty")
        elif self.front.next == None:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
        
    #Peek front
    def peek_front(self):
        if self.front == None:
            return RuntimeError("Empty")
        else:
            return self.front.data
        
    #print values to verify working
    def print_values(self):
        while self.front is not None:
            print(self.peek_front())
            self.dequeue()


    
