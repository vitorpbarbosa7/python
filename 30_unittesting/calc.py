def add(x, y):
    '''
    Adds two numbers
    '''
    return x + y

def subtract(x,y):
    '''
    Subtracts two numbers
    '''
    return x-y

def multiply(x, y):
    '''
    Multiplies two numbers
    '''
    return x*y

def divide(x, y):
    '''
    Divides two numbers
    '''
    if y == 0:
        raise ZeroDivisionError('Can not divide by zero!')
    return x / y