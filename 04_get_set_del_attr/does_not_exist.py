class Person:
	name = "Cristiano"
	goals = 900
	country = "Portugal"

worldCup = getattr(Person, 'worldCup', 'ChampionsLeague')
print(worldCup)
