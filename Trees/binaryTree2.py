'''
Created on May 26, 2013

@author: debanjan
'''
class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None
        
    def setRoot(self, root):
        self.root = root
        
    def getRoot(self):
        return self.root
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def insertLeftChild(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRightChild(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            

def preOrderTraversal(tree):
    if tree == None:
        return 
    else:
        print tree.root
        preOrderTraversal(tree.leftChild)
        preOrderTraversal(tree.rightChild)
        
        
r = BinaryTree('a')
#print r.getRoot()
#print(r.getLeftChild())
leftChild = BinaryTree("b")
leftChild.insertLeftChild("d")
r.insertLeftChild(leftChild)
#print(r.getLeftChild())
#print(r.getLeftChild().getRoot())
rightChild = BinaryTree("c")
rightChild.insertLeftChild("e")
rightChild.insertRightChild("f")
r.insertRightChild(rightChild)
#print(r.getRightChild())
#print(r.getRightChild().getRoot())
#r.getRightChild().setRoot('hello')
#print(r.getRightChild().getRoot()) 
           
            

preOrderTraversal(r)

