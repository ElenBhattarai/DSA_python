class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.recInsert(value,self.root)

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

    def inOrder(self):
        self.recInOrder(self.root)
    
    def recInOrder(self,curNode):
        if curNode is not None:
            self.recInOrder(curNode.leftChild)
            print(curNode.data)
            self.recInOrder(curNode.rightChild)