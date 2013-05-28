'''
Created on May 11, 2013

@author: debanjan
'''
class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0   
        
    
    def insert(self,element):
        self.items.append(element)
        
    def remove(self):
        
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i]>self.items[maxi]:
                maxi = i
        item = self.items[maxi]
#            self.items[maxi:maxi+1] = []
        self.items.remove(self.items[maxi])
        return item
        
    def print_queue(self):
        print self.items
        
q = PriorityQueue()
q.insert(11)
q.insert(12)
q.insert(14)
q.insert(13)

q.print_queue()
print q.remove()
while not q.is_empty(): 
    print q.remove()
#            
        