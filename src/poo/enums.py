import enum

# Direcoes = enum.Enum('Direcoes', [ 'ESQUERDA', 'DIREITA', 'ACIMA','ABAIXO'])
class Direcoes(enum.Enum):
	ESQUERDA = enum.auto() # 1
	DIREITA = enum.auto() # 2
	ACIMA = enum.auto() # 3
	ABAIXO = enum.auto() # 4 
	

def mover(direcao: Direcoes):
	# if direcao not in ['esquerda','direita','abaixo','acima']:
	if not isinstance(direcao, Direcoes):
		raise ValueError('Direcao nao encontrada')

	print(f'Movendo para {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)