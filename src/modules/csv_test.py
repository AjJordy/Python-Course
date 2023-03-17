import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'example.csv'
print(CAMINHO_CSV)


# --------------- Lendo CSV ------------------------
with open(CAMINHO_CSV, 'r', encoding='utf8') as file:
	# leitor = csv.reader(file) # list
	leitor = csv.DictReader(file) # dict

	# print(next(leitor))
	for linha in leitor:
		print(linha)


# --------------- Escrevendo CSV ------------------------
lista_clientes = [
	{'Nome': 'Luiz Otávio', 'Idade': '32', 'Endereço': 'Av Brasil, 21, Centro'}, 
	{'Nome': 'João da Silva', 'Idade': '55', 'Endereço': 'Rua 22, 44, Nova Era'}
]

with open(CAMINHO_CSV, 'w') as file:
	colunas = lista_clientes[0].keys()
	escritor = csv.writer(file)
	escritor.writerow(colunas)

	for cliente in lista_clientes:
		escritor.writerow(cliente.values())

# Easy way
with open(CAMINHO_CSV, 'w') as file:
	colunas = lista_clientes[0].keys()
	escritor = csv.DictWriter(file, fieldnames=colunas)
	escritor.writeheader()

	for cliente in lista_clientes:
		escritor.writerow(cliente)

