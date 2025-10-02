import time, random

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

def insert_into_sorted(mylist: list, element: int):
    for i in range(len(mylist)):
        if element < mylist[i]:
            mylist.insert(i, element)
            return
    mylist.append(element)

def generate_unsorted_list():
    unsorted_list = []
    for i in range(10000):
        unsorted_list.append(random.randint(1, 10000))
    return unsorted_list

def time_sort(sorting_method, mylist):
    start = time.time()
    sorted_list = sorting_method(mylist.copy()) 
    end = time.time()
    elapsed_time = end - start
    return sorted_list, elapsed_time

def main():
    sort_list = generate_unsorted_list()
    bubble_sort_result, bubble_elapsed = time_sort(bubble_sort, sort_list)

    insertion_sort_result, insertion_elapsed = time_sort(insertion_sort, sort_list)

    print(f"Insertion: Sorted list in {bubble_elapsed:.4f} seconds")
    print(f"Bubble: Sorted list in {insertion_elapsed:.4f} seconds")

main()