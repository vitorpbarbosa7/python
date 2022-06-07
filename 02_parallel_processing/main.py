from multiprocessing import Pool
from multiprocessing import cpu_count
from functools import partial
from IPython.display import display

from generate_data import generate_data
from avg_price_each_reader import avg_price_per_reader
from parallel_singular_param import parallel_singular_param
from parallelize_section import parallelize_section

from simple_genre_features import genre_features

if __name__ == "__main__":
    data = generate_data(dataset_size = 100000)
    display(data.sample(5))

    r_df = avg_price_per_reader(data)
    display(r_df.sample(5))

    CPU_COUNT = cpu_count()
    para_res = parallel_singular_param(data, avg_price_per_reader, CPU_COUNT)
    # print(type(para_res))
    display(para_res.sample(5))

    print(f"Genre features")
    reade_id_column = 'reader_id'
    readers = data['reader_id'].unique()
    g_df = genre_features(data, readers)
    display(g_df.sample(5))

    print(f"Parallelize multi argument section, with partial")
    parallelized_g_df = parallelize_section(genre_features, data, readers, CPU_COUNT)
    display(parallelized_g_df)