"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['João','Joana','Luiz','Letícia']
camisetas = [
	['preta','branca'],
	['p','m','g'],
	['masculino','feminino']
]

def print_iter(iterator):
	print(*list(iterator), sep='\n')
	print()

print('---- Combinations -----')
print_iter(combinations(pessoas, 2))
print_iter(combinations(pessoas, 3))

print('---- Permutations -----')
print_iter(permutations(pessoas, 2))
print_iter(permutations(pessoas, 3))

print('---- Product -----')
print_iter(product(*camisetas))


