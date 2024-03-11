import pandas as pd
import matplotlib.pyplot as plt
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from sorting_algorithms.insertion_sort import insertionSort

# Read the pickled benchmark results and return a dataframe
def read_benchmark_results(algorithm_name):
    file_path = f'results/{algorithm_name}.pkl'
    df = pd.read_pickle(file_path)
    return df

# Creating a new figure of defined size
def new_figure(height=55):
    return plt.figure(figsize=(84/25.4, height/25.4))

def generate_line_plot(df, title, xlabel, ylabel, file_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the 'size' against the specified columns
    df.plot(x='size', y=['sorted', 'reversed', 'random'], ax=ax, marker='o', linestyle='-')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(['Sorted', 'Reversed', 'Random'])

    plt.savefig(file_name, bbox_inches='tight')
    plt.show()

def generate_random_line_plot(algorithms, algorithm_dfs, title, xlabel, ylabel, file_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the 'size' against the 'random' column for each algorithm
    for algo, df in zip(algorithms, algorithm_dfs):
        ax.plot(df['size'], df['random'], marker='o', linestyle='-', label=algo)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

    plt.savefig(file_name, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_benchmark_results('mergeSort')
    quicksort_df = read_benchmark_results('quicksort')
    insertion_sort_df = read_benchmark_results('insertion_sort')

    x_values = merge_sort_df['size']

    # Generating and save line plot for Merge Sort
    generate_line_plot(merge_sort_df, title='Merge Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='mergesort_line_plot.pdf')

    # Generating and save line plot for Quick Sort
    generate_line_plot(quicksort_df, title='Quick Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='quicksort_line_plot.pdf')

    # Generating and save line plot for Insertion Sort
    generate_line_plot(insertion_sort_df, title='Insertion Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='insertionsort_line_plot.pdf')

    # Generating and save random line plot for all algorithms
    generate_random_line_plot(['Merge Sort', 'Quick Sort', 'Insertion Sort'],
                              [merge_sort_df, quicksort_df, insertion_sort_df],
                              title='Random Data Comparison',
                              xlabel='Input Size',
                              ylabel='Running Time',
                              file_name='random_comparison_line_plot.pdf')
