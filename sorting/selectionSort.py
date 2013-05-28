'''
Created on May 11, 2013

@author: debanjan
'''

itemList = [4,28,56,3,89,90,126]

    
def selection_sort(itemList):
    for i in range(0,len(itemList)-1):
        min = i
        for j in range(i+1,len(itemList)-1):
            if itemList[j] < itemList[i]:
                min = j
                
            if min != i:
                itemList[i], itemList[min] = itemList[min], itemList[i]
                
    return itemList

print selection_sort(itemList)
                