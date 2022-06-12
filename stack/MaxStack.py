from stack import Stack

class MaxStack:
    def __init__(self):
        self.mainStack = Stack()
        self.helperStack = Stack()
    
    def push(self, val: int) -> None:
        if self.mainStack.top is None:
            self.mainStack.push(val)
            self.helperStack.push(val)
        else:
            if val > self.helperStack.peek():
                self.mainStack.push(val)
                self.helperStack.push(val)
            else:
                self.mainStack.push(val)
                self.helperStack.push(self.helperStack.peek())
                
    def pop(self) -> None:
        self.helperStack.pop()
        return self.mainStack.pop()
    
    def top(self) -> int:
        return self.mainStack.peek()
        
    def getMax(self) -> int:
        return self.helperStack.peek()