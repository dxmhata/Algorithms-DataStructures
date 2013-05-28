'''
Created on May 26, 2013

@author: debanjan
'''
from Stacks import Stack
import binaryTree2



def buildParseTree(expression):
    pStack = []
    parseTree = binaryTree2.BinaryTree("")
    currentTree = parseTree
    exList = expression.split()
    print exList
    for i in exList:
        if i == "(":
            currentTree.insertLeftChild("")
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ["+","-","/","*"]:
            print str(i)
            currentTree.setRoot(str(i))
            if pStack == []:
                pass
            else:
                parent = pStack.pop()
                currentTree = parent
        elif i in ["+","-","/","*"]:
            currentTree.insertRightChild("")
            print i
            currentTree.setRoot(i)
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            if pStack == []:
                pass
            else:
                currentTree = pStack.pop()
        else:
            raise ValueError
    return parseTree


def inorder_traversal(parseTree):
    expression = ""
    if parseTree:
        expression = "("+inorder_traversal(parseTree.getLeftChild())
        expression = expression + str(parseTree.getRoot())
        expression = expression + inorder_traversal(parseTree.getRightChild())+")"
        
    return expression


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print inorder_traversal(pt)
        
