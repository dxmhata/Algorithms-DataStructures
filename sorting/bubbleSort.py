mylist = [12, 5, 13, 8,8, 9,9, 10, 65]

def bubble(List):
    
    unsorted = True

    while unsorted:
        for element in range(0,len(List)-1):
            unsorted = False
            if List[element] > List[element + 1]:
                temp = List[element + 1]
                List[element + 1] = List[element]
                List[element] = temp

            else:
                unsorted = True
    return list

print bubble(mylist)