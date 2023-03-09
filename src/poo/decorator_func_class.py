

def meu_repr(self) -> str:
	class_name = self.__class__.__name__
	class_dict = self.__dict__		
	return f'{class_name}({class_dict})'


def meu_planeta(metodo):
	def interno(self, *args, **kwargs):
		resultado = metodo(self, *args, **kwargs)
		if 'Terra' in resultado:
			return 'Você está em casa'
		return resultado
	return interno
	

def adiciona_repr(cls):
	cls.__repr__ = meu_repr
	return cls


class MyReprMixin:
	def __repr__(self) -> str:
		class_name = self.__class__.__name__
		class_dict = self.__dict__		
		return f'{class_name}({class_dict})'

@adiciona_repr
class Time: #(MyReprMixin):
	def __init__(self, nome) -> None:
		self.nome = nome

@adiciona_repr	
class Planeta: #(MyReprMixin):
	def __init__(self, nome) -> None:
		self.nome = nome

	@meu_planeta
	def falar_nome(self):
		return f'O planeta é {self.nome}'


# Time = adiciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

print(brasil)
print(portugal)

# Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())