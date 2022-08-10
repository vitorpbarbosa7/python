import gc

# future garbage
amount=10 # python interpreter should remove this garbage with the garbage collector
amount=5
print(amount)

x=200
print(x)
type(x)
x = 'Delhi'
print(x)
type(x)

gc.collect()
