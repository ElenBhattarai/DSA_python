class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    #constructor
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
    
    #size of linkedlist
    def size(self):
        return self.num_of_nodes

    #insert in a linkedlist
    def insert(self,index,data):
        if(index < 0 or index > self.size()):
            raise IndexError("Index Error")
        else:
            new_node = Node(data)
            #inserting at the beggining
            if(index == 0):
                new_node.next = self.head
                self.head = new_node
            #inserting at the end
            elif(index == self.size()):
                jumper_node = self.head

                while(jumper_node.next is not None):
                    jumper_node = jumper_node.next
                
                jumper_node.next = new_node
            #insert at an index
            else:
                one_before_node = self.head
                one_after_node = self.head

                for i in range(index-1):
                    one_before_node = one_before_node.next
                
                one_after_node = one_before_node.next

                one_before_node.next = new_node
                new_node.next = one_after_node
                
            self.num_of_nodes+=1

    #remove at an index
    def remove(self,index):
        if(index < 0 or index > self.size()-1):
            raise IndexError("Index error")
        else:
            #remove at the beggining
            if(index == 0):
                self.head = self.head.next
            
            #remove at the end
            elif(index == self.size() - 1):
                jumper_node = self.head
                for i in range(index-1):
                    jumper_node = jumper_node.next
                
                jumper_node.next = None
            
            #remove at any index
            else:
                one_before_node = self.head

                for i in range(index-1):
                    one_before_node = one_before_node.next
                
                one_after_node = one_before_node.next.next
                
                one_before_node.next = one_after_node
            
            self.num_of_nodes-=1
    
    #set an entry at index that already exists
    def set_entry(self, index, data):
        if(index < 0 or index > self.size()-1):
            raise IndexError("Index error")
        else:
            jumper_node = self.head
            for i in range(index):
                jumper_node = jumper_node.next
            
            jumper_node.data = data
    
    #clear the linkedlist
    def clear(self):
        self.head = None


    #print all the values in the linkedlist to verify everything works
    def print_values(self):
        if self.head is None:
            print(0)
        else:
            jumper_node = self.head
            count = 0
            while(jumper_node is not None):
                print(jumper_node.data)
                count+=1
                jumper_node = jumper_node.next
            print("Length is: ", count)

        
        
        
            




            



    