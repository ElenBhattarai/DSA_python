class QueueFromStacksRecursion:
    def __init__(self):
        self.recursiveStack = []
    
    def enqueue(self,value):
        self.recursiveStack.append(value)

    def dequeue(self):
        #base case find the first stack inserted value
        if len(self.recursiveStack) == 1:
            return self.recursiveStack.pop()
        
        #keep popping until the first item
        item = self.recursiveStack.pop()
        
        #recurse until found the last one
        dequeued_item = self.dequeue()

        #after finding item, reconstruct the stack
        self.recursiveStack.append(item)

        #the item we removed
        return dequeued_item

