from abc import ABC, abstractmethod

class Notificacao(ABC):
	def __init__(self, mensagem) -> None:
		self.mensagem = mensagem

	@abstractmethod
	def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
	def enviar(self) -> bool:
		print('Email enviado:', self.mensagem)
		return True
	

class NotificacaoSMS(Notificacao):
	def enviar(self) -> bool:
		print('SMS enviadA:', self.mensagem)
		return True


"""
From L of SOLID 
- Liskov Substitution principle
"""
notificacao = NotificacaoSMS('hello') # NotificacaoEmail('hello')
notificacao.enviar()

print('-'*20)

def notificar(notificacao: Notificacao):
	ret = notificacao.enviar()
	if ret:
		print('Enviado')
	else:
		print('Nao enviado')


notificar(NotificacaoSMS('SMS'))
notificar(NotificacaoEmail('email'))