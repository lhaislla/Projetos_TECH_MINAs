class Pessoa:
	def __init__(self, nome):
		self.nome = nome
	def say_hello(self):
		print('Olá, ' + self.nome)

class Studante(Pessoa):
	def __init__(self, nome, escola):
		super().__init__(nome)
		self.escola = escola
	def sing_escola_song(self):
		print('Para ' + self.escola)

studante = Studante('Lhaislla', 'UVM')
studante.say_hello()
studante.sing_escola_song()
# What are you?
print(isinstance(studante, Studante))
print(isinstance(studante, Pessoa))
print(issubclass(Studante, Pessoa))
