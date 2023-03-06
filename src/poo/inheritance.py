

class Pessoa:
	def __init__(self, nome) -> None:
		self.nome = nome

class Cliente(Pessoa):
	...

c1 = Cliente('Pedro')
print(c1.nome)