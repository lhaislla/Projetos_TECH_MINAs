class apresentador():
	def __init__(self, name):
		# Constructor
		self.name = name
	def say_hello(self):
		# method
		print('Hello, ' + self.name)

apresentador = apresentador('Chris')
apresentador.name = 'Christopher'
apresentador.say_hello()