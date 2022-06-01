class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    #push
    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    #peek
    def peek(self):
        if self.top == None:
            raise RuntimeError("Empty")
        else:
            return self.top.data
    
    #pop
    def pop(self):
        if self.top == None:
            raise RuntimeError("Empty")
        else:
            self.top = self.top.next

    #print all the values to check
    def print_values(self):
        while self.top is not None:
            print(self.peek())
            self.pop()

