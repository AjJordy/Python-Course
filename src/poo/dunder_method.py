# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def __add__(self, other):
		novo_x = self.x + other.x
		novo_y = self.y + other.y
		return Ponto(novo_x, novo_y)

	def __gt__(self, other):
		resultado_self = self.x + self.y
		resultado_other = other.x + other.y
		return resultado_self > resultado_other

	def __str__(self) -> str:
		return f'(x={self.x}, y={self.y})'

	def __repr__(self) -> str:
		# class_name = self.__class__.__name__
		class_name = type(self).__name__
		return f'{class_name}(x={self.x}, y={self.y})'


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p1))
print(p2)
print(f'{p2!r}')

print('-'*20)
p3 = p1 + p2
print(p3)
print('p2 e maior que p1 ? ', p2 > p1)