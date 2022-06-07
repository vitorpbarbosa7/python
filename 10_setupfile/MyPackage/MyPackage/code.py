import pandas as pd

class DummyClass:

	def __init__(self, word:str):
		self.word = word

	def show_data(self):
		'''
		Shows data from a pandas dataframe
		'''
		data = pd.read_csv("data/data.csv")
		print(data)

	def show_word(self):
		print(self.word)

	def return_word(self):
		return self.word