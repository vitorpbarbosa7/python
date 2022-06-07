import pandas as pd
import numpy as np
from functools import partial
from multiprocessing import cpu_count
from multiprocessing import Pool

def parallelize_section(fn, d, readers, n_cores):
    '''
    This function will parallelize a given input function which has multiple parameters
    as arguments. It will use the number of cores specified by the user. If the user 
    specifies more cores than availalbe on the computer, the function will raise a value error.
    
    params:
        fn (Function) : The function you want to run in parallel
        d (DataFrame) : The dataframe parameter of the function
        readers (List) : The readers parameter of the function 
        n_cores (Integer) : The number of cores you want to use
        
    example:
        readers = d.reader_id.unique()
        para_g_df = parallelize_section(genre_features, d, readers, 4)
    '''
    if cpu_count() < n_cores:
        raise ValueError("The number of CPU's specified exceed the amount available")

    reader_list = np.array_split(readers, n_cores)
    pool = Pool(n_cores)
    calc_df = pool.map(partial(fn, d), reader_list)
    pool.close()
    pool.join()
    
    return pd.concat(calc_df)