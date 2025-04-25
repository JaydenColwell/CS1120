# Project No.: 6
# Author: Jayden Colwell
# Description:
import random
import matplotlib.pyplot as plt
import time
from sys import setrecursionlimit

setrecursionlimit(5000)

def main():
    lengths = [10, 50, 100, 500, 1000]

    bubble_times = list()
    insert_times = list()

    for length in lengths:
        bubble_times.append(timing(bubble_sort, length))
        insert_times.append(timing(bubble_sort, length))

    show_results(bubble_times, insert_times)

def insertion_sort(data, n = None):
    if n is None:
        n = len(data)
    if n <= 1:
        return

    insertion_sort(data, n-1)

    temp = data[n-1]
    j = n - 2
    while j >= 0 and data[j] > temp:
        data[j+1] = data[j]
        j -= 1

    data[j+1] = temp

def bubble_sort(data, n = None):
    if n is None:
        n = len(data)
    if n <= 1:
        return

    swapped = False
    for i in range(n - 1):
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            swapped = True

    if swapped:
        bubble_sort(data, n-1)

def show_results(bubble_times, insert_times):
    time_data = {
        "Bubble sort" : bubble_times,
        "Insertion sort" : insert_times
    }
    x_vals = [10, 50, 100, 500, 1000]
    for i in range(len(bubble_times)):
        if bubble_times[i] > insert_times[i]:
            better = "Bubble sort"
        else:
            better = "Insertion sort"
        print(f'For a list of length {x_vals[i]}, {better} is faster')
        print(f'Bubble sort time: {bubble_times[i]:.4e}s Insertion sort time: {insert_times[i]:.4e}s')
        print(f'difference: {abs(bubble_times[i] - insert_times[i]):.4e} seconds Percent: {(abs(bubble_times[i] - insert_times[i])/(min([bubble_times[i], insert_times[i]]))* 100):.2f}% better\n')

    plt.figure(figsize=(10,6))
    for sort, times in time_data.items():
        plt.plot(x_vals, times, marker='.', label=sort)

    plt.title("Bubble Sort vs Insertion Sort")
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.xticks(x_vals)
    plt.ylim(0, 0.05)
    plt.yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05])
    plt.grid(True, linestyle="--")
    plt.legend()
    plt.show()

def timing(algorithm, length):
    times = []
    trials = 1000
    for _ in range(trials):
        arr = [random.randint(1,length) for _ in range(length)]
        start = time.perf_counter()
        algorithm(arr)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = sum(times) / trials
    return avg_time

main()