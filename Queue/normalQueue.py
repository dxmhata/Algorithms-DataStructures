class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
        
    def __str__(self):
        return str(self.cargo)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
    def isEmpty(self):
        return self.length == 0
    
    def insert(self,element):
        node = Node(element)
        node.next = None
                
        if self.length == 0:
            self.head = self.tail = node
        else:
            lastNode = self.tail
            lastNode.next = node
            self.last = node
        
        self.length += 1
        
    def remove(self):
        element = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return element
    
    def print_queue(self):
        pointer = self.head
        qList = []
        while(pointer):
            qList.append(pointer.cargo)
            pointer = pointer.next
            
        print qList
            
    

q = Queue()
q.insert(2)
q.insert(3)
q.print_queue()
print q.remove()
        
        
        
        