import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Read the results from pkl file and preprocess
def read_preprocess_results(algorithm_name):
    file_path = f'results/variance_{algorithm_name}.pkl'
    df = pd.read_pickle(file_path)

    # Calculating the mean execution time for each array size
    mean_times = df.mean(axis=0)

    # Calculating the standard error of the mean for each array size
    std_err = df.std(axis=0) / np.sqrt(len(df))

    # Calculating the degrees of freedom
    degrees_of_freedom = len(df) - 1

    # Calculating the confidence intervals using t-distribution
    confidence = 0.95
    confidence_intervals = std_err * t.interval(confidence, degrees_of_freedom)[1]

    # Creating a new dataframe with columns for array size, mean time, and confidence intervals
    data = pd.DataFrame({'Size': mean_times.index, 'Mean Time': mean_times.values, 'CI': confidence_intervals})

    return data

# Plot mean with the variance
def plot_variance(preprocessed_df, algorithm_name):
    plt.figure(figsize=(10, 6))
    plt.errorbar(preprocessed_df['Size'], preprocessed_df['Mean Time'], yerr=preprocessed_df['CI'], fmt='-o')
    plt.fill_between(preprocessed_df['Size'], preprocessed_df['Mean Time'] - preprocessed_df['CI'],
                     preprocessed_df['Mean Time'] + preprocessed_df['CI'], color='lightblue')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.grid(True)
    plt.savefig(f'{algorithm_name}_varianceplot.pdf')
    plt.show()

if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_preprocess_results('mergeSort')
    quicksort_df = read_preprocess_results('quicksort')
    insertion_sort_df = read_preprocess_results('insertionSort')

    # Plot variance for each algorithm
    plot_variance(merge_sort_df, 'Merge Sort')
    plot_variance(quicksort_df, 'Quick Sort')
    plot_variance(insertion_sort_df, 'Insertion Sort')
