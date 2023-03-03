from pprint import pprint

"""
lista = []
for numero in range(10):
	lista.append(numero * 2)
print(lista)
"""

lista = [numero * 2 for numero in range(10)]
print(lista)


""" Mapeamento """
produtos = [
	{'nome':'p1','preco':10},
	{'nome':'p2','preco':20},
	{'nome':'p3','preco':30},
]

nomes_produtos = [produto['nome'] for produto in produtos]
pprint(nomes_produtos)

novos_produtos = [
	{ **produto, 'preco': produto['preco']*1.05 }
	if produto['preco'] > 20 else {**produto}
	for produto in produtos
]
pprint(novos_produtos) # aumento de 5% no preço


"""  Filtro  """
lista = [ n for n in range(10) if n < 5 ]
pprint(lista)