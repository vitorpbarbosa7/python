class Employee: 
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'a'
emp_1.last = 'aa'

emp_2.first = 'b' 
emp_2.last = 'bb'

print(emp_1.first)
print(emp_2.first)
