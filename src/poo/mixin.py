from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

# Classe abstrata
# Padrão de projeto: Template method
class Log:
	def _log(self, msg):
		raise NotImplementedError('Implemente o método log')

	def log_error(self, msg):
		return self._log(f'Error: {msg}')

	
	def log_success(self, msg):
		return self._log(f'Success: {msg}')

class LogFileMixin(Log):
	def _log(self, msg):
		msg_formatada = f'{msg} ({self.__class__.__name__})'
		with open(LOG_FILE, 'a') as file:
			print(f'Salvando no log: {msg_formatada}')
			file.write(msg_formatada)
			file.write('\n')


class LogPrintMixin(Log):
	def _log(self, msg):
		print(f'Print: {msg}')


class Eletronico: 
	def __init__(self, nome) -> None:
		self._nome = nome
		self._ligado = False

	def ligar(self):
		if not self._ligado:
			self._ligado = True

	def desligar(self):
		if self._ligado:
			self._ligado = False


# Herança multipla
class Smartphone(Eletronico, LogPrintMixin): 

	def ligar(self):
		super().ligar()
		if self._ligado:
			self.log_success('Ligado')
	
	def desligar(self):
		super().desligar()
		if not self._ligado:
			self.log_success('Desligado')


if __name__ == '__main__':

	# lp = LogPrintMixin()
	# lp.log_error('oh no')
	# lp.log_success('ebaa')

	# lf = LogFileMixin()
	# lf.log_error('qualquer coisa')
	# lf.log_success('que legal')

	galaxy_s = Smartphone('Galaxy S')
	iphone = Smartphone('IPhone')
	galaxy_s.ligar()
	iphone.ligar()
	
