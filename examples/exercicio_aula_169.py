"""
Exercicio - Unir listas
Crie um função zipper 
o trabalho dessa função será unir duas 
listas na ordem

Use todos os valores da menor lista
Ex: 
['Salvador','Ubatuba','Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador','BA'),('Ubatuba','SP'),('Belo Horizonte','MG')]
"""

from itertools import zip_longest


lista_1 = ['Salvador','Ubatuba','Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista_1, lista_2):
	lenght = min(len(lista_1), len(lista_2))
	return [ 
		(lista_1[i], lista_2[i]) for i in range(lenght) 
	]
	
print('Meu zipper:\t',zipper(lista_1, lista_2))
print('Zip python:\t',list(zip(lista_1, lista_2)))
print('longest:\t', list(zip_longest(lista_1, lista_2, fillvalue='Sem cidade')))







