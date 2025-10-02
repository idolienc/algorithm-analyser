import time, random
import matplotlib.pyplot as plt
from collections.abc import Callable

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

def insert_into_sorted(mylist: list, element: int) -> None:
    for i in range(len(mylist)):
        if element < mylist[i]:
            mylist.insert(i, element)
            return
    mylist.append(element)

def generate_unsorted_list(size: int) -> list:
    unsorted_list = []
    for i in range(size):
        unsorted_list.append(random.randint(1, 1000000))
    return unsorted_list

def time_sort(sorting_method: Callable[[list], list], mylist: list) -> tuple[list, float]:
    copied_list = mylist.copy()
    start = time.perf_counter_ns()
    sorted_list = sorting_method(copied_list) 
    end = time.perf_counter_ns()
    elapsed_time = end - start
    return sorted_list, elapsed_time

def graph_efficiency(element_count: list, sort_times_one: list, sort_times_two: list):
    plt.plot(element_count, sort_times_one, marker='o')
    plt.plot(element_count, sort_times_two, marker='o')
    plt.title('Sort Efficiency Comparison')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (seconds)')
    plt.xticks(element_count, rotation=45)
    plt.ylim(0, max(sort_times_one) * 0.9)
    plt.xscale("log")
    plt.grid(True)
    plt.show()

def main():
    element_count = [100, 250, 500, 1000, 5000, 10000]
    unsorted_lists = []

    insertion_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        insertion_sort_result, insertion_elapsed = time_sort(insertion_sort, unsorted_lists[i])
        print(f"Insertion: Sorted list in {insertion_elapsed:.4f} seconds")
        insertion_times.append(insertion_elapsed)
    print(insertion_times)

    bubble_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        bubble_sort_result, bubble_elapsed = time_sort(bubble_sort, unsorted_lists[i])
        print(f"Bubble: Sorted list in {bubble_elapsed:.4f} seconds")
        bubble_times.append(bubble_elapsed)
    print(bubble_times)

    graph_efficiency(element_count, insertion_times, bubble_times)

main()