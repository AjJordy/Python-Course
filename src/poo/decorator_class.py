# Classes decoradoras 
class Multiplicar:
	def __init__(self, func) -> None:
		self.func = func
		self._multiplicador = 10

	def __call__(self, *args, **kwargs):		
		resultado = self.func(*args, **kwargs)
		return resultado * self._multiplicador


@Multiplicar
def soma(x, y):
	return x + y

dois_mais_dois = soma(2, 2)
print(dois_mais_dois)