# Assignment 1 
# Name: Charan deep Gopishetty
# Student ID: 169470218
# Date: 2025-06-21

"""
This script implements and analyzes the performance of five sorting algorithms:
Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort.

It includes:
- Step 1: Verifying correctness of sorting
- Step 2: Measuring T(n) (operation count) for best, average, and worst cases
- Step 3: Plotting T(n) vs n for worst case inputs
- Step 4: Plotting actual execution time vs n for worst case inputs
"""

import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

# Sorting algorithms with operation counting
def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            steps += 1
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3
    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
        steps += 3
    return steps

def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        steps += 2
        comparison_steps = 0
        while j >= 0 and key < my_list[j]:
            comparison_steps += 1
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 2
        steps += comparison_steps + 1
        my_list[j + 1] = key
        steps += 1
    return steps

def merge_sort(my_list):
    steps = 0
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        steps += len(my_list)
        steps += merge_sort(left_half)
        steps += merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            steps += 1
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
            steps += 1
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
            steps += 1
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
            steps += 1
    return steps

def _partition(my_list, low, high):
    steps = 0
    pivot = my_list[high]
    i = low - 1
    steps += 2
    for j in range(low, high):
        steps += 1
        if my_list[j] <= pivot:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
            steps += 4
    my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
    steps += 3
    return i + 1, steps

def _quick_sort_helper(my_list, low, high):
    steps = 0
    if low < high:
        pi, partition_steps = _partition(my_list, low, high)
        steps += partition_steps
        steps += _quick_sort_helper(my_list, low, pi - 1)
        steps += _quick_sort_helper(my_list, pi + 1, high)
    return steps

def quick_sort(my_list):
    return _quick_sort_helper(my_list, 0, len(my_list) - 1)

def step1_initial_test():
    print("--- Step 1: Sorting Functionality Check ---")
    original = [random.randint(0, 1000) for _ in range(100)]
    reference = sorted(original)
    funcs = {
        "Bubble": bubble_sort, "Selection": selection_sort,
        "Insertion": insertion_sort, "Merge": merge_sort, "Quick": quick_sort
    }
    for name, func in funcs.items():
        test = original[:]
        func(test)
        result = "Passed" if test == reference else "Failed"
        print(f"{name} Sort: {result}")

def step2_tn_analysis():
    print("\n--- Step 2: T(n) Analysis ---")
    size = 20
    avg = [random.randint(0, 100) for _ in range(size)]
    best = sorted(avg)
    worst = sorted(avg, reverse=True)
    funcs = {
        "Bubble": bubble_sort, "Selection": selection_sort,
        "Insertion": insertion_sort, "Merge": merge_sort, "Quick": quick_sort
    }
    for name, func in funcs.items():
        print(f"\n{name} Sort:")
        print(f"Best Case:    {func(best[:])}")
        print(f"Average Case: {func(avg[:])}")
        print(f"Worst Case:   {func(worst[:])}")

def step3_and_4_plotting():
    print("\n--- Step 3 & 4: Generating and Saving Plots ---")
    quad_sizes = [10, 50, 100, 250, 500, 1000, 2500]
    nlogn_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    funcs = {
        "Bubble": (bubble_sort, quad_sizes),
        "Selection": (selection_sort, quad_sizes),
        "Insertion": (insertion_sort, quad_sizes),
        "Quick": (quick_sort, quad_sizes),
        "Merge": (merge_sort, nlogn_sizes),
    }
    tns, times = {k: [] for k in funcs}, {k: [] for k in funcs}
    for name, (func, sizes) in funcs.items():
        for n in sizes:
            worst = list(range(n)) if name == "Quick" else list(range(n, 0, -1))
            tns[name].append(func(worst[:]))
            start = time.perf_counter()
            func(worst[:])
            end = time.perf_counter()
            times[name].append(end - start)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 16))
    for name in tns:
        ax1.plot(funcs[name][1], tns[name], marker='o', label=name)
    ax1.set_title("Step 3: Operation Count T(n) vs List Size")
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlabel("List Size (n)")
    ax1.set_ylabel("T(n)")
    ax1.grid(True)
    ax1.legend()

    for name in times:
        ax2.plot(funcs[name][1], times[name], marker='o', label=name)
    ax2.set_title("Step 4: Execution Time vs List Size")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("List Size (n)")
    ax2.set_ylabel("Time (seconds)")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.savefig("sorting_analysis_plots.png", dpi=300)
    plt.show()
    print("Graphs saved as 'sorting_analysis_plots.png'.")

if __name__ == "__main__":
    step1_initial_test()
    step2_tn_analysis()
    step3_and_4_plotting()
