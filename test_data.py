import numpy as np

rng = np.random.seed(72) #use for creating test data with a seed
increase_factor = 2
num_lengths = 14
# might have to change length for the different algorithms. 
# length of 14 goes up to 8000
# length of 12 goes up to 2000

# initialize an array contaning the different array sizes that will be benchmarked
data_lengths = np.zeros(num_lengths).astype("int64")
data_lengths[0] = 1
for i in range(1, num_lengths):
    data_lengths[i] = data_lengths[i-1]*increase_factor

# Initialize empty arrays
random_arrs  = np.empty((num_lengths, ), dtype=object)
sorted_arrs  = np.empty((num_lengths, ), dtype=object)
reversed_arrs = np.empty((num_lengths, ), dtype=object)

# Fill arrays with random, sorted and reverse sorted values
for idx, length in enumerate(data_lengths):
    random_arrs[idx] = np.random.uniform(size=length)  
    sorted_arrs[idx] = np.arange(length)
    reversed_arrs[idx] = sorted_arrs[idx][::-1]
    
test_data = {"random": random_arrs, "sorted": sorted_arrs, "reversed": reversed_arrs}