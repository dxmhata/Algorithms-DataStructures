'''
Created on May 9, 2013

@author: debanjan
'''
class Tree:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)
    
    

def print_tree(tree):
    if tree == None :
        return
    print tree.element
    print_tree(tree.left)
    print_tree(tree.right)
    
    
def inorder_traversal(tree):
    if tree == None:
        return
    inorder_traversal(tree.left)
    print tree.element
    inorder_traversal(tree.right)
    
    
def postorder_traversal(tree):
    if tree == None:
        return
    postorder_traversal(tree.right)
    postorder_traversal(tree.left)
    print tree.element

def tree_sum(tree):
    if tree == None:
        return 0
    return tree_sum(tree.left)+tree_sum(tree.right)+tree.element  

def height(tree):
    if tree == None:
        return 0
    else:
        return max(height(tree.left),height(tree.right)) + 1  

#def print_tree_indented(tree, level=0):
#    if tree == None:
#        return
#    print       
def inorder_traversal_with_height(tree):
    if tree == None:
        return
    print "Current height of the tree:", height(tree)
    print "Current node of the tree:",tree.element
    print "Height of the left subtree:",height(tree.left)
    print "Height of the right subtree:",height(tree.right)
    print "Difference in height:", abs(height(tree.right)-height(tree.left))
    inorder_traversal(tree.left) 
    inorder_traversal(tree.right) 


tree = Tree(1,Tree(2,Tree(4),Tree(5)),Tree(3))

print_tree(tree)

inorder_traversal(tree)
postorder_traversal(tree)
print tree_sum(tree)
print height(tree)
inorder_traversal_with_height(tree)
