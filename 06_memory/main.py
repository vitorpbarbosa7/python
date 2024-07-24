import numpy as np

x = 10
y = x
z = 10

print(x)

print('x', hex(id(x)))
print('y', hex(id(y)))

x = x + 1

print('x', hex(id(x)))
print('y', hex(id(y)))

print('z', hex(id(z)))

print('python has dynamic typing')
z = 'a'
print('z', z)
