'''
Created on May 11, 2013

@author: debanjan
'''
import random
from random import randrange

mylist = [12, 5, 13, 8,8, 9,9, 10, 65]

def qsort1(mylist):

    if mylist == []:
        return []
    else:
        pivot = mylist[0]
        lesser = qsort1([x for x in mylist[1:] if x < pivot])
        greater = qsort1([x for x in mylist[1:] if x >= pivot])
        return lesser + [pivot] + greater
    

print qsort1(mylist)


def partition(mylist, l, e, g):
    while mylist != []:
        head = mylist.pop(0)
        if head < e[0]:
            l = [head] + l
        if head > e[0]:
            g = [head]+ g
        if head == e[0]:
            e = [head] + e
            
    return (l,e,g)

def qsort2(mylist):
    if mylist == []:
        return []
    else:
        pivot = mylist[0]
        lesser,equal,greater = partition(mylist[1:],[],list([pivot]),[])
        return qsort2(lesser)+equal+qsort2(greater)
    
print qsort2(mylist)


def qsort1a(list):

    def qsort(list):
        if list == []: 
            return []
        else:
            pivot = list.pop(randrange(len(list)))
            lesser = qsort([l for l in list if l < pivot])
            greater = qsort([l for l in list if l >= pivot])
            return lesser + [pivot] + greater
    return qsort(list[:])

print qsort1a(mylist)

            