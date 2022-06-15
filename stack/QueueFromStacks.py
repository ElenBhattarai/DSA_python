from stack import Stack

class QueueFromStacks:
    def __init__(self):
        self.enqueueStack = Stack()
        self.dequeueStack = Stack()
    
    def enqueue(self,value):
        self.enqueueStack.push(value)

    def dequeue(self):
        if ((self.dequeueStack.top is None) and (self.enqueueStack.top is None)):
            raise RuntimeError("Queue is empty")
        else:
            if self.dequeueStack.top is None:
                while(self.enqueueStack.top is not None):
                    self.dequeueStack.push(self.enqueueStack.peek())
                    self.enqueueStack.pop()
                print(self.dequeueStack.peek())
                self.dequeueStack.pop()
            else:
                print(self.dequeueStack.peek())
                self.dequeueStack.pop()
    
