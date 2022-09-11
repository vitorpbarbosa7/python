class AirPlane():
	def __init__(self, model):
		self.model = model

	def rotate(self):
		print(f'rotating')


rainha = AirPlane('747') 

rotate = getattr(rainha, 'rotate')
rotate()

def fly_forever():
	print('flying forever')

land = getattr(rainha, 'land', fly_forever())
land
