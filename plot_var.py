import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from matplotlib.backends.backend_pdf import PdfPages


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
    data = pd.DataFrame({'Size': mean_times.index, 'Mean Time (sec)': mean_times.values, 'CI': confidence_intervals})

    return data

# Plot mean with the variance
def plot_variance(preprocessed_dfs, algorithm_names):
    plt.figure(figsize=(10, 6))
    plt.rcParams.update({'font.size': 18})

    # Plotting each algorithm's variance
    for preprocessed_df, algorithm_name in zip(preprocessed_dfs, algorithm_names):
        plt.errorbar(preprocessed_df['Size'], preprocessed_df['Mean Time (sec)'], yerr=preprocessed_df['CI'],
                     fmt='-o', label=algorithm_name)
        plt.fill_between(preprocessed_df['Size'], preprocessed_df['Mean Time (sec)'] - preprocessed_df['CI'],
                         preprocessed_df['Mean Time (sec)'] + preprocessed_df['CI'], alpha=0.3)

    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.rcParams.update({'font.size': 18})
    plt.grid(True)
    plt.savefig('figures/variance_plot.pdf')
    plt.show()

def add_ci_columns(df):
    df['CI Lower'] = df['Mean Time (sec)'] - df['CI']
    df['CI Higher'] = df['Mean Time (sec)'] + df['CI']
    return df

def create_pdf_table_per_algorithm(df, algorithm_name, decimal_places=4):
    # Rounding the numerical values
    df_rounded = df.round(decimal_places)

    # Create and style the table
    fig, ax = plt.subplots(figsize=(8, 0.5 * len(df_rounded)))
    ax.axis('off')
    table = ax.table(cellText=df_rounded.values, colLabels=df_rounded.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    # Styling the table
    for k, cell in table._cells.items():
        cell.set_edgecolor('black')
        if k[0] == 0 or k[1] < 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#40466e')
        else:
            cell.set_facecolor('white')

    # Save the table as a PDF
    pdf_file = f'figures/{algorithm_name}_performance_summary.pdf'
    plt.savefig(pdf_file, bbox_inches='tight', pad_inches=0.1)
    plt.close()


if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_preprocess_results('mergeSort')
    quicksort_df = read_preprocess_results('quicksort')
    insertion_sort_df = read_preprocess_results('insertionSort')

    # Plot variance for each algorithm
    plot_variance([merge_sort_df, insertion_sort_df, quicksort_df], ['Merge Sort', 'Insertion Sort', 'Quick Sort'])

    for algorithm in ['mergeSort', 'quicksort', 'insertionSort']:
        df = read_preprocess_results(algorithm)
        df_with_ci = add_ci_columns(df)
        create_pdf_table_per_algorithm(df_with_ci, algorithm)

