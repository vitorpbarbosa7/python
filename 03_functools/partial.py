from functools import partial

def multiply(x, y, z):
        return x * y * z

# create a new function that multiplies by 2
dbl = partial(partial(multiply, 2),2)
print(dbl(2))
