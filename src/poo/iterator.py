
from collections.abc import Sequence  # Iterable


class MyList(Sequence):

	def __init__(self) -> None:
		self._data = {}
		self._index = 0
		self._next_index = 0	

	def __iter__(self):
		return self

	def __next__(self):
		if self._next_index >= self._index:
			self._next_index = 0
			raise StopIteration

		value = self._data[self._next_index]
		self._next_index += 1
		return value


	def __len__(self):
		return self._index

	def __getitem__(self, index):
		return self._data[index]

	def __setitem__(self, index, value):
		self._data[index] = value



	def append(self, value):
		self._data[self._index] = value
		self._index += 1




if __name__ == '__main__':
	lista = MyList()
	lista.append('Maria')
	lista.append('Luiz')
	print(lista._data)
	lista[0] = 'Joao'
	print(lista[0])
	print(len(lista))

	for item in lista:
		print(item)