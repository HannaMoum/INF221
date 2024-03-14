import numpy as np
import timeit
from copy import copy
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.merge_sort import mergeSort
from sorting_algorithms.insertion_sort import insertionSort
from test_data import generate_test_data
import pandas as pd

def benchmark(sorting_algorithm):
    """ 
    Benchmark the sorting_algorithm by running for various array sizes, determined in the "generate_test_data" function.
    Also, benchmark average, best- and worst case.
    The number of executions is limited depedendent on the arra size to prevent benchmarking from taking an unneccessary long time.
    """
    data_lengths, test_data = generate_test_data(sorting_algorithm)

    repeat = 5 # number of repetitions we will perform
    df = pd.DataFrame({"size": data_lengths}) # will store all benchmark times in this dataframe
    n = len(data_lengths)

    if sorting_algorithm.__name__ == "insertionSort":
        stmt = "sort_func(copy(data))"
    else:
        stmt = "sort_func(copy(data), 0, len(data)-1)"

    for name, data in test_data.items(): # benchmark for all random, sorted and reversed arrays
        run_times = np.empty(n) # will store running times for each iteration
        print(name)
        
        # perform sorting for all array sizes
        for i in range(n): 
            print("Running array size", len(data[i]))

            # Set up timer with algorithm and data
            clock = timeit.Timer(stmt=stmt, 
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

    df.to_pickle("results/" + sorting_algorithm.__name__ + ".pkl") # upload benchmarking to pickle file


def benchmark_with_variance(sorting_algorithm):
    """ Benchmark the sorting_algorithm by running for various array sizes, determined in the "generate_test_data" function.
    Save all times for each execution for each array size to get an idea of the variance in running times.
    Only the randomly ordered arrays are considered here.
    The number of executions is limited differently for the different sorting algorithms due to 
    the difference in efficiency for the algorithms.
    """
    data_lengths, test_data = generate_test_data(sorting_algorithm)
    df = pd.DataFrame(columns = data_lengths) # will store all benchmark times in this dataframe
            # each column represents all times measured for one array size marked by the columnname

    if sorting_algorithm.__name__ == "insertionSort":
        stmt = "sort_func(copy(data))"
        n_executions = 30
    elif sorting_algorithm.__name__ == "mergeSort":
        stmt = "sort_func(copy(data), 0, len(data)-1)"
        n_executions = 300
    elif sorting_algorithm.__name__ == "quicksort":
        stmt = "sort_func(copy(data), 0, len(data)-1)"
        n_executions = 10000
    else:
        raise AttributeError ("The provided sorting algorithm is not defined")

    for data in test_data["random"]: # benchmark for all random, sorted and reversed arrays
        print('running array size: ', len(data))
        # Set up timer with algorithm and data
        clock = timeit.Timer(stmt=stmt, 
                            globals={"sort_func": sorting_algorithm, # function to time
                                    "data": data, # input array to sort
                                    "copy": copy # copy function, needed to make fresh copy of array every time
                            }  
        )

        run_times = np.empty(n_executions) # will store running times for each iteration
        # perform timing
        for i in range(n_executions):
            run_times[i] = clock.timeit(1) 

        df[len(data)] = run_times # update dataframe
    
    df.to_pickle("results/variance_" + sorting_algorithm.__name__ + ".pkl") # upload benchmarking to pickle file


if __name__ == "__main__":
    # Decide which algorithms to benchmark
    #benchmark(insertionSort)
    #benchmark(mergeSort)
    #benchmark(quicksort)
    #benchmark_with_variance(insertionSort)
    benchmark_with_variance(mergeSort)
    #benchmark_with_variance(quicksort)
    