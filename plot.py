import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from sorting_algorithms.insertion_sort import insertionSort


# Read the pickled benchmark results, and return a dataframe
def read_benchmark_results(algorithm_name):
    file_path = f'results/{algorithm_name}.pkl'
    df = pd.read_pickle(file_path)

    if algorithm_name == "quicksort":
        df = df.assign(theoretical_avg = (df['size'] * np.log2(df['size'])) / 100000)
        df = df.assign(theoretical_bst = (df['size'] * np.log2(df['size'])) / 100000)
        df = df.assign(theoretical_wrs = (df['size']^2) / 100000)

    elif algorithm_name == "insertionSort":
        df = df.assign(theoretical_avg = (df['size']^2) / 1000)
        df = df.assign(theoretical_bst=(df['size'] * np.log2(df['size'])) / 1000)
        df = df.assign(theoretical_wrs=(df['size'] ^ 2) / 1000)
    else:
        df = df.assign(theoretical_avg = (df['size'] * np.log2(df['size'])) / 1000000)
        df = df.assign(theoretical_bst=(df['size'] * np.log2(df['size'])) / 1000000)
        df = df.assign(theoretical_wrs=(df['size'] ^ 2) / 1000000)

    return df


# Creating a new figure of defined size
def new_figure(height=55):
    return plt.figure(figsize=(84/25.4, height/25.4))


def generate_plot(df, xlabel, ylabel, file_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the 'size' against the specified columns
    df.plot(x='size', y=['sorted', 'reversed', 'random'], ax=ax, marker='o', linestyle='-')
    df.plot(x='size', y=['theoretical_avg', 'theoretical_bst', 'theoretical_wrs'], ax=ax, marker='', linestyle='-', color='black')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.savefig(file_name, bbox_inches='tight')
    plt.show()


def generate_random_plot(algorithms, algorithm_dfs, xlabel, ylabel, file_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the 'size' against the 'random' column for each algorithm
    for algo, df in zip(algorithms, algorithm_dfs):
        ax.plot(df['size'], df['random'], marker='o', linestyle='-', label=algo)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.savefig(file_name, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_benchmark_results('mergeSort')
    quicksort_df = read_benchmark_results('quicksort')
    insertion_sort_df = read_benchmark_results('insertionSort')

    # Generating and save line plot for Merge Sort
    generate_plot(merge_sort_df, xlabel='Input Size', ylabel='Running Time',
                  file_name='mergesort_line_plot.pdf')

    # Generating and save line plot for Quick Sort
    generate_plot(quicksort_df, xlabel='Input Size', ylabel='Running Time',
                  file_name='quicksort_line_plot.pdf')

    # Generating and save line plot for Insertion Sort
    generate_plot(insertion_sort_df, xlabel='Input Size', ylabel='Running Time',
                  file_name='insertionsort_line_plot.pdf')

    # Generating and save random line plot for all algorithms
    generate_random_plot(['Merge Sort', 'Quick Sort', 'Insertion Sort'],
                         [merge_sort_df, quicksort_df, insertion_sort_df],
                         xlabel='Input Size',
                         ylabel='Running Time',
                         file_name='random_comparison_line_plot.pdf')
