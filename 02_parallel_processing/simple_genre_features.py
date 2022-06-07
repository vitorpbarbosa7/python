import pandas as pd 
import numpy as np

def genre_features(d, readers, genre_col = 'book_genre', reader_col = 'reader_id'):
    '''
    The following function will generate a normalized 1 hot encoding associated to the 
    genres each user has read.
    
    params:
        d (DataFrame) : The dataset which holds the reader and book history
        readers (List) : The list of reader_id's
        genre_col (String) : The column in d which is associated to the book genre
        reader_col (String) : The column in d which is associated to the reader col
        
    example:
        readers = d.reader_id.unique()
        g_df = genre_features(d, readers)
    '''
    
    res = []
    for reader in readers:
        g = d[d[reader_col] == reader][genre_col].value_counts(normalize = True).to_dict()
        df = pd.DataFrame([g], index = [reader])
        res.append(df)
    return pd.concat(res).fillna(0)