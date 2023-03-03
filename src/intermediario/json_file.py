import json


pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}


with open('test.json', 'w', encoding='utf-8') as file:
	json.dump(pessoa, file, ensure_ascii=False, indent=4)


with open('test.json', 'r', encoding='utf-8') as file:
	print(json.load(file))