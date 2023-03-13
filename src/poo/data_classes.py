# Facilita com a criação de  __init__ , __repr__, __eq__

from dataclasses import dataclass, asdict, astuple, field

@dataclass(order=True) # (init=False)
class Pessoa: 
	nome: str = 'Missing'
	sobrenome: str = field(default='Missing')
	idade: int = 100
	enderecos: list[str] = field(default_factory=list)

	
	# def __init__(self, nome, sobrenome) -> None:
	# 	self.nome = nome
	# 	self.sobrenome = sobrenome		


	def __post_init__(self):
		self.nome_completo = f'{self.nome} {self.sobrenome}'


	@property
	def nome_completo(self):
		return f'{self.nome} {self.sobrenome}'

	@nome_completo.setter
	def nome_completo(self, value):
		nome , *sobrenome = value.split()
		self.nome = nome
		self.sobrenome = ' '.join(sobrenome)


@dataclass(frozen=True)
class ClasseConstante:
	nome: str
	sobrenome: str


if __name__ == '__main__':
	p1 = Pessoa('Luiz', 'Silva')
	print(p1)
	# p1.nome_completo = "Maria Helena Figueiredo"
	# print(p1)

	const = ClasseConstante('Lucas', 'Silva')
	# const.nome = "Luiz" # Error: cannot assign to field 'nome'

	lista = [Pessoa('A','Z'), Pessoa('B','Y'), Pessoa('C','X')]

	ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome)
	print(ordenadas)


	print('asdict:',asdict(p1))
	print('astuple:',astuple(p1))
