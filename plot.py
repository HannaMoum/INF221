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

# Generating and saving a plot
def generate_plot(x, y, title, xlabel, ylabel, file_name):
    fig = new_figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.errorbar(x, y['mean'], yerr=y['std'], fmt='o-', label=title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    fig.savefig(file_name, bbox_inches='tight')

if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_benchmark_results('mergeSort')
    quicksort_df = read_benchmark_results('quicksort')
    #insertion_sort_df = read_benchmark_results('insertion_sort')

    print(merge_sort_df.columns)
    print(quicksort_df.columns)

    # Assuming all dataframes have the same 'size' column
    x_values = merge_sort_df['size']

    # Generating and save plot for mergeSort
    generate_plot(x_values, merge_sort_df[['random', 'sorted', 'reversed']],
                  title='Merge Sort', xlabel='Input Size', ylabel='Running Time',
                  file_name='merge_sort_plot.pdf')

    # Generating and save plot for quicksort
    generate_plot(x_values, quicksort_df[['random', 'sorted', 'reversed']],
                  title='Quicksort', xlabel='Input Size', ylabel='Running Time',
                  file_name='quicksort_plot.pdf')

    # Generating and save plot for insertion sort
    generate_plot(x_values, insertion_sort_df[['random', 'sorted', 'reversed']],
                  title='Insertion Sort', xlabel='Input Size', ylabel='Running Time',
                  file_name='insertion_sort_plot.pdf')
