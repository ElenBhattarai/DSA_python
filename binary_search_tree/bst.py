class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None
    
    #insert
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.recInsert(value,self.root)

    #recursive helper method for insert
    def recInsert(self,value,curNode):
        if(curNode.data == value):
            raise RuntimeError("Duplicates arent allowed")
        elif(curNode.data > value):
            if(curNode.leftChild is None):
                curNode.leftChild = Node(value)
            else:
                self.recInsert(value, curNode.leftChild)
        else:
            if(curNode.rightChild is None):
                curNode.rightChild = Node(value)
            else:
                self.recInsert(value, curNode.rightChild)

    #search
    def search(self,value):
        return self.recSearch(value,self.root)
    
    #recursive helper method for search
    def recSearch(self,value,curNode):
        if curNode is None:
            raise RuntimeError("Did not find matching data")
        elif curNode.data == value:
            return curNode.data
        else:
            if curNode.data > value:
                return self.recSearch(value, curNode.leftChild)
            else:
                return self.recSearch(value, curNode.rightChild)
    
    #remove
    def remove(self,value):
        self.root = self.recRemove(value,self.root)
    
    #recursive helper for remove
    def recRemove(self, value, curNode):
        if(curNode == None):
            raise RuntimeError("did not find matching data")
        elif curNode.data > value:
            curNode.leftChild = self.recRemove(value, curNode.leftChild)
        elif curNode.data < value:
            curNode.rightChild = self.recRemove(value,curNode.rightChild)
        else:
            if(curNode.rightChild is None and curNode.leftChild is None):
                curNode = None
            elif not curNode.leftChild:
                return curNode.rightChild
            elif not curNode.rightChild:
                return curNode.leftChild
            else:
                temp = self.findMinFromRight(curNode.rightChild)
                curNode.data = temp.data
                curNode.rightChild = self.recRemove(temp.data, curNode.rightChild)
        return curNode

    #find the minimum from right subtree
    def findMinFromRight(self,curNode):
        if curNode.leftChild is None:
            return curNode
        else:
            return self.findMinFromRight(curNode.leftChild)

    #in order traversal
    def inOrder(self):
        self.recInOrder(self.root)
    
    def recInOrder(self,curNode):
        if curNode is not None:
            self.recInOrder(curNode.leftChild)
            print(curNode.data)
            self.recInOrder(curNode.rightChild)
    
    #pre order traversal
    def preOrder(self):
        self.recPreOrder(self.root)
    
    def recPreOrder(self,curNode):
        if curNode is not None:
            print(curNode.data)
            self.recPreOrder(curNode.leftChild)
            self.recPreOrder(curNode.rightChild)
    
    #post order traversal
    def postOrder(self):
        self.recPostOrder(self.root)
    
    def recPostOrder(self,curNode):
        if curNode is not None:
            self.recPostOrder(curNode.leftChild)
            self.recPostOrder(curNode.rightChild)
            print(curNode.data)