
class Carro:
	def __init__(self, nome) -> None:
		self.nome = nome

	def acelerar(self):
		print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
celta = Carro(nome='Celta')

fusca.acelerar()
celta.acelerar()