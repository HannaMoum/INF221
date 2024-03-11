import numpy as np
import timeit
from copy import copy
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from test_data import data_lengths, test_data
import pandas as pd

def benchmark(sorting_algorithm):
    repeat = 5 # number of repetitions we will perform
    df = pd.DataFrame({"size": data_lengths}) # will store all benchmark times in this dataframe
    n = len(data_lengths)
    for name, data in test_data.items(): # benchmark for all random, sorted and reversed arrays
        run_times = np.empty(n) # will store running times for each iteration
        print(name)
        
        # perform sorting for all array sizes
        for i in range(n): 
            print(i)

            # Set up timer with algorithm and data
            clock = timeit.Timer(stmt="sort_func(copy(data), 0, len(data)-1)", 
                                globals={"sort_func": sorting_algorithm, # function to time
                                        "data": data[i], # input array to sort
                                        "copy": copy # copy function, needed to make fresh copy of array every time
                                }  
            )

            n_executions, t = clock.autorange() # how many executions can we make before time > (0.2 -> 0.5, might depend on computer)
            n_executions *= 3 # closer to 1 second than 0.2
            # perform timing
            time = clock.repeat(repeat=repeat, 
                                number=n_executions
                                ) # number of executions, repeated 5 times
             
            run_times[i] = sum(time)/(n_executions*repeat) # average value for each execution considering all the repetitions
        df[name] = run_times # add columns for benchmarking random, sorted and reversed arrays

    df.to_pickle(sorting_algorithm.__name__ + ".pkl") # upload benchmarking to pickle file

if __name__ == "__main__":
    # Decide which algorithm to benchmark
    benchmark(mergeSort)