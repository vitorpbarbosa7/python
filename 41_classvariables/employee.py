
class Employee:

    # class variable (not a instance variable)
    # the same for all instances
    # possible to access when the class is instantiated also
    # but the same for all
    raise_amt = 1.04 

    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)


emp_1 = Employee('Alan', 'Turing', 50000)
emp_2 = Employee('John', 'Neumann', 60000)

# can access the class variable like this:
print(Employee.raise_amt)
# can also access like this
# from the instance itself
print(emp_1.raise_amt)

print(emp_1.pay)

print(emp_1.raise_amt)
emp_1.apply_raise()
print(emp_2.pay)
