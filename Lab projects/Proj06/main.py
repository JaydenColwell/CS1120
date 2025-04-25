# Project No.: 6
# Author: Jayden Colwell
# Description: Compares the time performance of bubble sort and insertion sort over lists of size 10, 50, 100, 500, and 1000.
# Uses random ints and gets the average time over 1000 tests for each algorithm for each size.
import random
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time
from sys import setrecursionlimit
# Increases recursion limit to allow for the list with size 1000.
setrecursionlimit(5000)

def main():
    # Creates list lengths and empty time lists for each type.
    lengths = [10, 50, 100, 500, 1000]
    bubble_times = list()
    insert_times = list()
    # Adds the average time of each sort for each length of list.
    for length in lengths:
        bubble_times.append(timing(bubble_sort, length))
        insert_times.append(timing(bubble_sort, length))
    # Calls function to show results with matplotlib and in terminal.
    show_results(bubble_times, insert_times)

def insertion_sort(data, n = None):
    # sets n to list size on first call and base case of n is 1 or less.
    if n is None:
        n = len(data)
    if n <= 1:
        return
    # Recursive call with length - 1.
    insertion_sort(data, n-1)
    # Gets item to be sorted and loops through data to find it's sorted point.
    temp = data[n-1]
    j = n - 2
    while j >= 0 and data[j] > temp:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = temp

def bubble_sort(data, n = None):
    # sets n to list size on first call and base case of n is 1 or less.
    if n is None:
        n = len(data)
    if n <= 1:
        return
    # Loops through list sorting adjacent items.
    swapped = False
    for i in range(n - 1):
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            swapped = True
    # Recursive call only if any elements swapped on last pass.
    if swapped:
        bubble_sort(data, n-1)

def show_results(bubble_times, insert_times):
    # Creates dictionary and length list for access later.
    time_data = {
        "Bubble sort" : bubble_times,
        "Insertion sort" : insert_times
    }
    x_vals = [10, 50, 100, 500, 1000]
    # Output for terminal comparing times for each length of list.
    for i in range(len(bubble_times)):
        if bubble_times[i] > insert_times[i]:
            better = "Bubble sort"
        else:
            better = "Insertion sort"
        print(f'For a list of length {x_vals[i]}, {better} is faster')
        print(f'Bubble sort time: {bubble_times[i]:.4e}s Insertion sort time: {insert_times[i]:.4e}s')
        print(f'difference: {abs(bubble_times[i] - insert_times[i]):.4e} seconds Percent: {(abs(bubble_times[i] - insert_times[i])/(min([bubble_times[i], insert_times[i]]))* 100):.2f}% better\n')

    # Creates matplotlib figure and splits into 2 for the graph and table.
    fig = plt.figure(figsize=(12, 10))
    gs = GridSpec(2, 1, height_ratios=[2, 1])
    # Creates the table and attaches to the plot.
    ax_plot = fig.add_subplot(gs[0])
    for sort, times in time_data.items():
        ax_plot.plot(x_vals, times, marker='.', label=sort)

    ax_plot.set_title("Bubble Sort vs Insertion Sort")
    ax_plot.set_xlabel("List length")
    ax_plot.set_ylabel("Time (s)")
    ax_plot.set_xticks(x_vals)
    ax_plot.set_ylim(0, 0.05)
    ax_plot.set_yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05])
    ax_plot.grid(True, linestyle="--")
    ax_plot.legend()
    # Creates list of data for easy use on the table.
    ax_table = fig.add_subplot(gs[1])
    ax_table.axis("off")
    table_data = list()
    table_data.append(["List size"] + list(time_data.keys()))
    for i, size in enumerate(x_vals):
        row = [str(size)]
        for sort_alg in list(time_data.keys()):
            row.append(f'{time_data[sort_alg][i]:.4e}s')
        table_data.append(row)
    # Creates the table and attaches to the plot.
    table = ax_table.table(
        cellText=table_data,
        loc="center",
        cellLoc="center",
        colColours=["#f0f0f0"] * (len(list(time_data.keys())) + 1),
        edges="B"
    )
    table.scale(0.4,1.2)
    # Saves plot as png and displays it.
    plt.savefig("comparison_graph_and_table.png", dpi=300)
    plt.show()

def timing(algorithm, length):
    # Creates empty list of times and sets the number of trials for each run.
    times = []
    trials = 1000
    # Creates a list of random ints of the length requested.
    # Starts timer, runs sort, stops time and adds to list.
    for _ in range(trials):
        arr = [random.randint(1,length) for _ in range(length)]
        start = time.perf_counter()
        algorithm(arr)
        end = time.perf_counter()
        times.append(end - start)
    # Returns average time from all the trials.
    avg_time = sum(times) / trials
    return avg_time

main()