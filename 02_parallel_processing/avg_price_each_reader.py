import pandas as pd
import numpy as np

def avg_price_per_reader(data):
    '''
    This function will calculate the average book price associated to each reader
    
    params:
        data (DataFrame) : The dataset holding the reader history and book price
        
    example:
        r_df = avg_price_per_reader(d)
    '''
    readers = data.reader_id.unique()
    res = []
    for reader in readers:
        avg_price = np.mean(data[data['reader_id'] == reader].book_price.values)
        r_df = {
            'reader_id' : reader,
            'avg_price' : avg_price
        }
        res.append(r_df)
    return pd.DataFrame(res)