import time, random, itertools
import matplotlib.pyplot as plt
from collections.abc import Callable
from typing import TypeVar

T = TypeVar('T')

def bubble_sort(lst: list[T]) -> None:
    """Sorts a list in-place by comparing elements 
    and swapping them if the elements are in the wrong order.

    Time complexity is O(n^2).
    """
    for i in range(len(lst)-1):
        for j in range(len(lst)-(1+i)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def insertion_sort(lst: list[T]) -> list[T]:
    """Sorts an unsorted list by inserting elements
    in order into a new list, which is returned by the function.

    Time complexity is O(n^2)
    """
    sorted_list = []
    for element in lst:
        insert_into_sorted(sorted_list, element)
    return sorted_list

def insert_into_sorted(lst: list[T], element: T) -> None:
    """Modifies an already ascendingly sorted list 
    in-place by inserting a new element while maintaining 
    the sort order.
    """
    for i in range(len(lst)):
        if element < lst[i]:
            lst.insert(i, element)
            return
    lst.append(element)

def generate_unsorted_list(size: int) -> list[int]:
    """Generates an unsorted list containing 
    integers ranging from 1 to 1,000,000
    """
    unsorted_list = []
    for i in range(size):
        unsorted_list.append(random.randint(1, 1000000))
    return unsorted_list

def timer(sorting_method: Callable[[list], list], lst: list) -> tuple[list, float]:
    """Times how long it takes for each sorting method to sort a list, if incorrectly
    ordered, and then return it. Returns the sorted list and elapsed time, in seconds, as a tuple.
    """
    copied_list = lst.copy()
    start = time.perf_counter_ns()
    sorted_list = sorting_method(copied_list) 
    end = time.perf_counter_ns()
    elapsed_time = (end - start) / 1_000_000_000  
    return sorted_list, elapsed_time

def graph_efficiency(element_count: list, **kwargs):
    """Plots a log-scaled comparison of execution times for two sorting algorithms 
    over varying input sizes.
    """
    plt.title('Sort Elapsed Time Comparison')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (seconds)')
    plt.xticks(element_count, rotation=45)
    plt.xscale("log")
    plt.ylim(0, max(max(values) for values in kwargs.values()) * 1.1)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    plt.grid(True)
    for arg in kwargs:
        plt.plot(element_count, kwargs[arg], label=(arg.replace("_", " ")).title(), marker='o')
    plt.legend(loc="upper left")
    plt.show()

def main():
    element_count = [100, 250, 500, 1000, 5000, 10000]
    unsorted_lists = []

    insertion_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        insertion_sort_result, insertion_elapsed = timer(insertion_sort, unsorted_lists[i])
        insertion_times.append(insertion_elapsed)

    bubble_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        bubble_sort_result, bubble_elapsed = timer(bubble_sort, unsorted_lists[i])
        bubble_times.append(bubble_elapsed)

    graph_efficiency(element_count, insertion_times=insertion_times, bubble_times=bubble_times)

if __name__ == "__main__":
    main()