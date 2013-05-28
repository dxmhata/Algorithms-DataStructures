'''
Created on May 11, 2013

@author: debanjan
'''
mylist = [12, 5, 13, 8,8, 9,9, 10, 65]

def merge(left, right):
    fullList = []
    
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            fullList.append(left[i])
            i += 1
        else:
            fullList.append(right[j])
            j += 1
            
    fullList += left[i:]
    fullList += right[j:]
    
    return fullList

def mergesort(lst):
    if len(lst) <=1:
        return lst
    else:
        middle = int(len(lst)/2)
        left = mergesort(lst[:middle])
        right = mergesort(lst[middle:])
        
        return merge(left,right)
    
print mergesort(mylist)