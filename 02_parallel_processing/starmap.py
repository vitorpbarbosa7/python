# https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments

#!/usr/bin/env python3
from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support

def func(a, b):
    return a + b

def main():
    a_args = [1,2,3]
    second_arg = 1
    with Pool() as pool:
        L = pool.starmap(func, [(1, 1), (2, 1), (3, 1)])
        print(L)
        M = pool.starmap(func, zip(a_args, repeat(second_arg)))
        print(M)
        N = pool.map(partial(func, b=second_arg), a_args)
        print(N)
        assert L == M == N

if __name__=="__main__":
    freeze_support()
    main()