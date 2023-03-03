

class Pessoa:
	def __init__(self, nome, sobrenome) -> None:
		self.nome = nome
		self.sobrenome = sobrenome


p1 = Pessoa('João', 'Silva')
p2 = Pessoa('Maria', 'Joana') 

print(f'{p1.nome} {p1.sobrenome}')
print(f'{p2.nome} {p2.sobrenome}')