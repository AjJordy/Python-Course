

class Caneta:

	def __init__(self, cor) -> None:
		self.cor_tinta = cor

	@property
	def cor(self):
		return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.cor)