import pandas as pd
import numpy as np
from multiprocessing import Pool
from multiprocessing import cpu_count

def parallel_singular_param(data, fn, n_cores):
    '''
    This function will run a function with a single argument in parallel depending on
    the number of cores the user has specified. If the user specifies more cores than
    availalbe on the computer, the function will raise a value error.
    
    params:
        d (DataFrame) : The argument for the function
        fn (Function) : The function you want to run in parallel
        n_cores (Integer) : The number of cores you want to use
        
    example:
        parallel_singular_param(
            d,
            avg_price_per_reader,
            4
        )
    '''
    if cpu_count() < n_cores:
        raise ValueError("The number of CPU's specified exceed the amount available")

    print(f"Initiliaze split")
    df_list = np.array_split(data, n_cores)
    print(f"Initialize pool")
    pool = Pool(n_cores)
    print(f"Execute pool")
    res = pool.map(fn, df_list)
    pool.close()
    pool.join()
    return pd.concat(res)