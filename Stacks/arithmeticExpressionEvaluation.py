'''
Created on Apr 10, 2013

@author: debanjan
'''

operationStack = []
valueStack = []
inp = raw_input("Provide an arithmetic expression:")

for char in inp:
    if char == "(":
        pass
    
    if char == "+":
        operationStack.append(char)
        print operationStack
    if char == "*":
        operationStack.append(char)
        print operationStack
    if char == "/":
        operationStack.append(char)
        print operationStack
    if char == "-":
        operationStack.append(char)
        print operationStack
    if char == ")":
        operation = operationStack.pop()
        value = valueStack.pop()
        
        if operation == "+":
            value = int(valueStack.pop())+int(value)
            valueStack.append(value)
            print valueStack
        if operation == "*":
            value = int(valueStack.pop()) * int(value)
            valueStack.append(value)
            print valueStack
        if operation == "/":
            value = int(valueStack.pop())/int(value)
            valueStack.append(value)
            print valueStack
        if operation == "-":
            value = int(valueStack.pop()) - int(value)
            valueStack.append(value)
            print valueStack
           
    if char not in ["/","+","-","*","(",")"]:
        valueStack.append((char))
        print valueStack
    
print valueStack
        
        
    