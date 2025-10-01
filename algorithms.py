def bubble_sort(mylist: list) -> list:
    for i in range(len(mylist)-1):
        for x in range(len(mylist)-(1+i)):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist

def insertion_sort(mylist: list) -> list:
    sortedlist = []
    for i in range(len(mylist)):
        insert_into_sorted(sortedlist, mylist[i])
    return sortedlist

def insert_into_sorted(the_list, element):
    for i in range(len(the_list)):
        if element < the_list[i]:
            the_list.insert(i, element)
            return
    the_list.append(element)