'''
Created on May 26, 2013

@author: debanjan
'''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return (len(self.items) == [])
    def peek(self):
        return self.items[len(self.items)-1]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)