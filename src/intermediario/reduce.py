from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 15},
    {'nome': 'Produto 1', 'preco': 20},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 15},
    {'nome': 'Produto 4', 'preco': 70},
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


total = reduce(
	lambda total, produto: total + produto['preco'] ,
	produtos,
	initial=0
)

print('total:', total)