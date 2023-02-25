import copy

produtos = [
	{'nome':'Produto 5', 'preco': 10.00},
	{'nome':'Produto 1', 'preco': 22.32},
	{'nome':'Produto 3', 'preco': 10.11},
	{'nome':'Produto 2', 'preco': 105.87},
	{'nome':'Produto 4', 'preco': 69.90},
]


# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy
novos_produtos = [ 
	{**produto, 'preco': round(produto['preco'] * 1.1, 2)}
	for produto in produtos
]
print('------ novos_produtos -----')
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente 
# Gere produtos_ordenados_por_nome por deep copy
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(
	key=lambda produto: produto['nome']
)
print('------ produtos_ordenados_por_nome ------')
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente
# Gere produtos_ordenados_por_preco por deep copy
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(
	key=lambda produto: produto['preco']
)
print('------ produtos_ordenados_por_preco ------')
print(*produtos_ordenados_por_preco, sep='\n')