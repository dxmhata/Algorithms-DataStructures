'''
Created on May 11, 2013

@author: debanjan
'''
itemList = [4,28,56,3,89,90,126]

def insertion_sort(itemList):
    for i in range(1,len(itemList)):
        value = itemList[i]
        j = i-1
        while (j >= 0):
            if value < itemList[j]:
                itemList[j+1] = itemList[j]
                itemList[j] = value
                j -= 1
            else:
                break
            
    return itemList

print insertion_sort(itemList)
            
def shellSort(array):
     "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
     gap = len(array) // 2
     # loop over the gaps
     while gap > 0:
         # do the insertion sort
         for i in range(gap, len(array)):
             val = array[i]
             j = i
             while j >= gap and array[j - gap] > val:
                 array[j] = array[j - gap]
                 j -= gap
             array[j] = val
         gap //= 2
         
     return array
 
print shellSort(itemList)
         
            

            
            
            
        