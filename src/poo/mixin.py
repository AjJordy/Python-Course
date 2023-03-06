from pathlib import Path

LOG_FILE = Path(__file__).parent / ''

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
		print(msg)


class LogPrintMixin(Log):
	def _log(self, msg):
		print(f'Print: {msg}')

l = LogFileMixin()
l.log_error('oh no')
l.log_success('ebaa')