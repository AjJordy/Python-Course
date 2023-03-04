# getter -> obter valor
# setter -> definir valor

"""
Python não tem modificadores de acesso, mas temos uma convenção
	(sem underline)  = public -> Todos tem acesso
 -	(um underline)	 = protected -> Apenas na classe e subclasses
 __ (dois underline) = private -> Apenas na classe
"""

class Caneta:

	def __init__(self, cor) -> None:
		# private protected 
		self._cor = cor

	@property
	def cor(self):
		return self._cor
	
	@cor.setter
	def cor(self, valor):
		self._cor = valor


caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Vermelho'
print(caneta.cor)