import pandas as pd
import matplotlib.pyplot as plt
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from sorting_algorithms.insertion_sort import insertionSort

# Read the pickled benchmark results, and return a dataframe
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
    df.plot(x='size', y=['sorted', 'resversed', 'random'], ax=ax, marker='o', linestyle='-')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(['Sorted', 'Reversed', 'Random'])

    plt.savefig(file_name, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_benchmark_results('mergeSort')
    quicksort_df = read_benchmark_results('quicksort')
    insertion_sort_df = read_benchmark_results('insertion_sort')

    # Assuming all dataframes have the same 'size' column
    x_values = merge_sort_df['size']

    # Generating and save line plot for Merge Sort
    generate_line_plot(merge_sort_df, title='Merge Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='mergesort_line_plot.pdf')

    # Generating and save line plot for Quick Sort
    generate_line_plot(quicksort_df, title='Quick Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='quicksort_line_plot.pdf')

    # Generating and save line plot for Insertion Sort
    generate_line_plot(quicksort_df, title='Insertion Sort', xlabel='Input Size', ylabel='Running Time',
                       file_name='insertionsort_line_plot.pdf')