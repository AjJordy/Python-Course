# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
import os
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
	title: str
	original_title: str
	is_movie: bool
	imdb_rating: float
	year: int 
	characters: list[str]
	budget: None | float


string_json = '''
{
	"title": "O Senhor dos Anéis: A Sociedade do Anel",
	"original_title": "The Lord of the Rings: The Fellowship of the Ring",
	"is_movie": true,
	"imdb_rating": 8.8,
	"year": 2001,
	"characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
	"budget": null
}
'''

# ------------------- strings --------------
filme: Movie = json.loads(string_json)
# pprint(filme)
# print(filme['title'])
# print(filme['characters'][0])
print(json.dumps(filme, ensure_ascii=False, indent=2))

# ------------------- arquivos --------------
NOME_ARQUIVO = 'example.json'
CAMINHO_ABS_ARQUIVO = os.path.abspath(
	os.path.join(
		os.path.dirname(__file__),
		NOME_ARQUIVO
	)
)

dict_filme = {
	'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
	'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
	'is_movie': True, 
	'imdb_rating': 8.8, 
	'year': 2001, 
	'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
	'budget': None
}


with open(CAMINHO_ABS_ARQUIVO, 'w') as file:
	json.dump(dict_filme, file, ensure_ascii=False, indent=2)

with open(CAMINHO_ABS_ARQUIVO, 'r') as file:
	filme_do_json = json.load(file)
	print(filme_do_json)