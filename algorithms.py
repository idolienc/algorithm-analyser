import time, random
import matplotlib.pyplot as plt
import mplcyberpunk
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

def insertion_sort(lst: list[T]) -> None:
    """Sorts a list in-place by building a sorted section
    on the left. Starting from the second element it swaps
    backwards until the element is correctly placed, repeating
    this until elements are correctly sorted.

    Time complexity is O(n^2)
    """
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
        i += 1

def merge_sort(lst: list[T]) -> list[T]:
    """Sorts a list by recursively splitting the input 
    list down into single elements, merging two
    sorted sublists until a fully sorted list is produced.

    Time complexity is O(n logn)
    """
    if len(lst) <= 1:
        return lst.copy()
    left_lst = merge_sort(lst[:len(lst)//2])  
    right_lst = merge_sort(lst[len(lst)//2:])  
    return merge(left_lst, right_lst)

def merge(left: list[T], right: list[T]) -> list[T]:
    """Merges two sorted lists into a single sorted list.
    Compares the smallest elements and appends the smaller one 
    to a new list. Continues until all elements are ordered. 
    Assumes both lists are already ordered.
    """
    result=[]
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result.extend(left[l_index:])
    result.extend(right[r_index:])
    return result

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
    plt.style.use('cyberpunk')
    plt.title('Sort Elapsed Time Comparison')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (seconds)')
    plt.xticks(element_count, rotation=45)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    plt.grid(True)
    for arg in kwargs:
        plt.loglog(element_count, kwargs[arg], label=(arg.replace("_", " ")).title(), marker='o')
    plt.legend(loc="upper left")
    mplcyberpunk.add_glow_effects()
    plt.show()

def main():
    element_count = [100, 250, 500, 1000, 5000, 10000]
    unsorted_lists = []

    insertion_times = []
    bubble_times = []
    merge_times = []
    for i in range(len(element_count)):
        unsorted_lists.append(generate_unsorted_list(element_count[i]))
        unsorted_insertion = unsorted_lists.copy()
        unsorted_bubble = unsorted_lists.copy()
        unsorted_merge = unsorted_lists.copy()
        insertion_sort_result, insertion_elapsed = timer(insertion_sort, unsorted_insertion[i])
        insertion_times.append(insertion_elapsed)

        bubble_sort_result, bubble_elapsed = timer(bubble_sort, unsorted_bubble[i])
        bubble_times.append(bubble_elapsed)

        merge_sort_result, merge_elapsed = timer(merge_sort, unsorted_merge[i])
        merge_times.append(merge_elapsed)

    graph_efficiency(element_count, insertion_times=insertion_times, bubble_times=bubble_times, merge_times=merge_times)

if __name__ == "__main__":
    main()