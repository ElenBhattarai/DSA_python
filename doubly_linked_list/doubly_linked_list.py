class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    #insert at the end of doubly linkedlist
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
    
    #insert at the front of doubly linkedlist
    def insert_at_start(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    #insert after certain value
    def insert_after_value(self,data,actualData):
        jumper = self.head
        found = False
        while jumper is not None:
            if jumper.data == data:
                found = True
                break
            jumper = jumper.next
        if(not found):
            raise RuntimeError("Not found entry")
        #entry found and is stored in jumper
        else:
            new_node = Node(actualData)
            one_after = jumper.next
            #if at last index
            if jumper.next == None:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
            else:
                jumper.next = new_node
                new_node.previous = jumper
                new_node.next = one_after
                one_after.previous = new_node

    #remove from front    
    def remove_from_front(self):
        if self.head is None:
            raise IndexError("Its empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

    #remove from back
    def remove_from_back(self):
        if self.head is None:
            raise IndexError("It's Empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
    
    #delete a value
    def delete_value(self,value):
        jumper = self.head
        while jumper is not None:
            if jumper.data == value:
                break
            jumper = jumper.next
        if jumper is None:
            raise RuntimeError("Doesnt exist")
        #value found
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None

            #if at first index:
            elif jumper.previous is None:
                self.head = self.head.next
                self.head.previous = None

            #if at last index
            elif jumper.next is None:
                self.tail = self.tail.previous
                self.tail.next = None
            
            else:
                previous_node = jumper.previous
                next_node = jumper.next
                previous_node.next = next_node
                next_node.previous = previous_node

    #Traverse from front
    def traverse_from_front(self):
        jumper = self.head
        while(jumper is not None):
            print(jumper.data)
            jumper = jumper.next
    
    #Traverse from back
    def traverse_from_back(self):
        jumper = self.tail

        while(jumper is not None):
            print(jumper.data)
            jumper = jumper.previous
    




            
