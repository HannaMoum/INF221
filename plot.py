import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from sorting_algorithms.insertion_sort import insertionSort
from matplotlib.backends.backend_pdf import PdfPages


# Read the pickled benchmark results, and return a dataframe
def read_benchmark_results(algorithm_name):
    file_path = f'results/{algorithm_name}.pkl'
    df = pd.read_pickle(file_path)
    # Ensure there are no non-positive sizes that could result in log(0)
    df = df[df['size'] > 0]
    return df

# Generate plot function
def generate_plot(df, algorithm, xlabel, ylabel, file_name):
    plt.rcParams.update({'font.size': 18})
    fig, ax = plt.subplots(figsize=(10, 6))

    # Filtering out rows where size is less than 2 to avoid log(1) which is 0
    df = df[df['size'] > 1]

    # Plot data
    df.plot(x='size', y=['sorted', 'reversed', 'random'], ax=ax, marker='o', linestyle='-', legend=False)

    # Theoretical complexities start at a size greater than 1
    sizes = df['size']
    first_size = sizes.iloc[0]
    first_random_time = df.iloc[0]['random']

    # Calculating normalization factors based on the first data point larger than 1
    norm_factor_n_log_n = first_random_time / (first_size * np.log2(first_size))
    norm_factor_n_square = first_random_time / (first_size ** 2)

    # Plot the theoretical complexities
    if algorithm in ['mergeSort', 'quicksort']:
        ax.plot(sizes, norm_factor_n_log_n * sizes * np.log2(sizes), label='O(n log n)', color='black', linestyle='--')
        if algorithm == 'quicksort':
            ax.plot(sizes, norm_factor_n_square * sizes ** 2, label='O(n^2) [worst]', color='black', linestyle='--')
    elif algorithm == 'insertionSort':
        ax.plot(sizes, norm_factor_n_square * sizes ** 2, label='O(n^2)', color='black', linestyle='--')
        ax.plot(sizes, first_random_time * sizes / first_size, label='O(n) [best]', color='black', linestyle='--')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.grid(True)
    plt.savefig(file_name, bbox_inches='tight')
    plt.show()

# Create a table in pdf
def create_pdf_table(df, algorithm_name, decimal_places=4):
    # Rounding the numerical values
    df = df.round(decimal_places)

    # Selecting some start, middle and end-rows
    start_rows = df.head(3)
    middle_rows = df.iloc[len(df)//2 - 1 : len(df)//2 + 2]
    end_rows = df.tail(3)

    # Combining these into a single dataframe
    summary_df = pd.concat([start_rows, middle_rows, end_rows])

    # Estimate figure size and creating the table
    table_height = 0.05 * len(summary_df) + 0.1
    fig, ax = plt.subplots(figsize=(8, table_height))
    ax.axis('off')
    table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.2)

    # Styling the table
    for k, cell in table._cells.items():
        if k[0] == 0:  # Header row
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor('#40466e')
        else:
            cell.set_facecolor('white')

    # Adjust layout and save to PDF
    pdf_file = f'{algorithm_name}_benchmark_summary.pdf'
    with PdfPages(pdf_file) as pdf:
        pdf.savefig(fig, bbox_inches='tight', pad_inches=0)

    plt.close(fig)


# Main function
if __name__ == "__main__":
    # Combining the benchmark results from different algorithms
    merge_sort_df = read_benchmark_results('mergeSort')
    quicksort_df = read_benchmark_results('quicksort')
    insertion_sort_df = read_benchmark_results('insertionSort')

    # Generating and save line plots
    generate_plot(merge_sort_df, 'mergeSort', 'Input Size', 'Running Time (sec)', 'mergesort_line_plot.pdf')
    generate_plot(quicksort_df, 'quicksort', 'Input Size', 'Running Time (sec)', 'quicksort_line_plot.pdf')
    generate_plot(insertion_sort_df, 'insertionSort', 'Input Size', 'Running Time (sec)', 'insertionsort_line_plot.pdf')

    # Creating PDF table for each algorithm
    create_pdf_table(merge_sort_df, 'Merge Sort')
    create_pdf_table(quicksort_df, 'Quick Sort')
    create_pdf_table(insertion_sort_df, 'Insertion Sort')