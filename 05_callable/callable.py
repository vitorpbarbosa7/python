'''
Every python function in python is a callable, meaning you're able to call it with the double open closed parentheses
https://www.pythonmorsels.com/callables/

So, not all "function"s that we think it is in python, are really functions, some are classes, but since we can call them, and execute some "action", we call it a function, 
but in a more general manner of saying, all are callables, like the enumerate "function", which in fact is a class
'''


class IntrovertedPlayer:
	def __init__(self, name, team):
		self.name = name
		self.team = team

	def __str__(self):
		return f'{self.name} is an introverted player at {self.team}'

class Player:
	def __init__(self, name, team):
		self.name = name
		self.team = team
	def __call__(self):
		print(f'{self.name} team is {self.team}')

messi = IntrovertedPlayer('messi', 'psg')
print(messi)

if callable(messi):
	messi()

haaland = Player('haaland', 'city')
haaland()
