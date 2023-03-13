# IMUTÁVEL 

# from collections import namedtuple
from typing import NamedTuple

# Carta = namedtuple(
# 	'Carta', ['valor','naipe'],
# 	defaults=['VALOR','NAIPE']
# )

class Carta(NamedTuple):
	valor: str = 'VALOR'
	naipe: str = 'NAIPE'



as_espadas = Carta('A','Espadas')
print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)
print(as_espadas._asdict())

# for valor in as_espadas:
# 	print(valor)
	