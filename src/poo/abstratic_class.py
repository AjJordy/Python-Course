from abc import ABC, abstractmethod


class Log(ABC):

	@abstractmethod
	def _log(self, msg): ...
		

	def log_error(self, msg):
		return self._log(f'Error: {msg}')

	
	def log_success(self, msg):
		return self._log(f'Success: {msg}')



class LogPrintMixin(Log):
	def _log(self, msg):
		print(f'Print: {msg}')


if __name__ == '__main__':
	# log = Log() # Cannot instantiate abstract class
	log = LogPrintMixin()
	log.log_success('Hello')