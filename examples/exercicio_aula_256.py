"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""



from abc import ABC, abstractmethod


class Conta(ABC):
	
	def __init__(self, agencia: int, conta: int, saldo: float=0) -> None:
		super().__init__()
		self._agencia = agencia
		self._conta = conta
		self._saldo = saldo 

	@abstractmethod
	def sacar(self, valor: float) -> bool: ...		
	
	def depositar(self, valor: float) -> float:
		self._saldo += valor
		self.detalhes(f'(DEPOSITO {valor})')
		return self._saldo

	def detalhes(self, msg: str='') -> None:
		print(f'O seu saldo é {self._saldo:.2f} {msg}\n-\n')

	def __repr__(self) -> str:
		return f'{self.__class__.__name__}({self._agencia}, {self._conta}, {self._saldo})'
		


class ContaCorrente(Conta):

	def __init__(self, agencia: int, conta: int, saldo: float=0, limite: float=0) -> None:
		super().__init__(agencia, conta, saldo)
		self._limite = limite

	def sacar(self, valor):
		super().sacar(valor)
		if self._saldo + self._limite >= valor:  
			self._saldo -= valor
			self.detalhes(f'(SAQUE {valor})')
			return True
		self.detalhes(f'Saque negado {valor}')		
		return False



class ContaPoupanca(Conta):

	def __init__(self, agencia: int, conta: int, saldo: float=0) -> None:
		super().__init__(agencia, conta, saldo)

	def sacar(self, valor: float) -> bool:
		super().sacar(valor)
		if self._saldo >= valor:  
			self._saldo -= valor
			self.detalhes(f'(SAQUE {valor})')
			return True
		self.detalhes(f'Saque negado {valor}')		
		return False



class Pessoa:

	def __init__(self, nome: str, idade: int) -> None:
		super().__init__()
		self.nome = nome
		self.idade = idade

	@property 
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome: str):
		self._nome = nome

	@property 
	def idade(self):
		return self._idade

	@idade.setter
	def idade(self, idade: int):
		self._idade = idade

	def __repr__(self) -> str:
		return f'Pessoa({self.nome!r}, {self.idade!r})'

class Cliente(Pessoa):

	def __init__(self, nome, idade) -> None:
		super().__init__(nome, idade)
		self.conta: Conta | None = None

	def __repr__(self) -> str:
		return super().__repr__()


	
class Banco():
	def __init__(
		self, 
		agencias: list[int] | None=None, 
		contas: list[Conta] | None=None,
		clientes: list[Pessoa] | None=None,
	) -> None:
		self.contas = contas or []
		self.clientes = clientes or []
		self.agencias = agencias or []

	def _checa_agencia(self, conta):
		if conta.agencia in self.agencias:
			return True
		return False

	
	def _checa_cliente(self, cliente):
		if cliente in self.clientes:
			return True
		return False

	def _checa_conta(self, conta):
		if conta.agencia in self.agencias:
			return True
		return False

		
	def autenticar(self, conta, cliente) -> bool:		
		return self._checa_agencia(conta) and \
			self._checa_cliente(cliente) and \
				self._checa_conta(conta)

	def __repr__(self) -> str:
		return f'Banco({self.agencias!r}, {self.clientes!r}, {self.contas!r})'




if __name__ == '__main__':
	...
	cp1 = ContaPoupanca(111, 222, 0)
	cp1.sacar(1)
	cp1.depositar(10)
	cp1.sacar(5)
	
	cc1 = ContaCorrente(111, 222, 0, 100)
	cc1.sacar(1)
	cc1.depositar(10)
	cc1.sacar(5)
	print(cc1)

	c1 = Cliente('Luiz', 30)
	print(c1)
	c1.conta = cc1

	banco = Banco()
	print(banco)

