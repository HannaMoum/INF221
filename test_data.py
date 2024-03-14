import numpy as np

def generate_test_data(sorting_algorithm):
    rng = np.random.seed(72) #use for creating test data with a seed
    increase_factor = 2

    if sorting_algorithm.__name__ == "quicksort":
        num_lengths = 10 # up tp length of 500
    else:
        num_lengths = 14 # up tp length of 8000

    # initialize an array contaning the different array sizes that will be benchmarked
    data_lengths = np.zeros(num_lengths).astype("int64")
    data_lengths[0] = 1
    for i in range(1, num_lengths):
        data_lengths[i] = data_lengths[i-1]*increase_factor

    # Initialize empty arrays
    random_arrs   = np.empty((num_lengths, ), dtype=object)
    sorted_arrs   = np.empty((num_lengths, ), dtype=object)
    reversed_arrs = np.empty((num_lengths, ), dtype=object)

    # Fill arrays with random, sorted and reverse sorted values
    for idx, length in enumerate(data_lengths):
        random_arrs[idx]   = np.random.uniform(size=length)  
        sorted_arrs[idx]   = np.arange(length)
        reversed_arrs[idx] = sorted_arrs[idx][::-1]
        
    test_data = {"random": random_arrs, "sorted": sorted_arrs, "reversed": reversed_arrs}
    return data_lengths, test_data
