def gennum(n):
	for i in range(n):
		yield i

gen = gennum(5)

for num in gen:
	print(num)
