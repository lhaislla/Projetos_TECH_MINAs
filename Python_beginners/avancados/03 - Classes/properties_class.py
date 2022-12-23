class Apresentador():
	def __init__(self, name):
		# Constructor
		self.name = name

	@property
	def name(self):
		print('Recuperando nome...')
		return self.__name
	@name.setter
	def name(self, value):
		# cool validation here
		print('Validatndo nome...')
		self.__name = value

apresentador = Apresentador('Lai')
apresentador.name = 'Lhaislla'
print(apresentador.name)