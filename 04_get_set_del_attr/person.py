class Person:
	name = "Messi"
	age = 35
	country = "Argentina"

x = getattr(Person, 'age')
print(x)
