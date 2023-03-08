from contextlib import contextmanager


class MyContextManager:

	def __init__(self, caminho_arquivo, modo) -> None:
		print('Init')
		self.caminho_arquivo = caminho_arquivo
		self.modo = modo
		self._file = None

	def __enter__(self):
		print('Abrindo arquivo')
		self._file = open(self.caminho_arquivo, self.modo, encoding='utf8')
		return self._file


	def __exit__(self, class_exception, exception_, traceback_):
		print('Fechando arquivo')
		self._file.close()
		# raise class_exception(*exception_.args).with_traceback(traceback_)
		# print(class_exception)
		# print(exception_)
		# print(traceback_)		
		return True
 
with MyContextManager('./teste.txt', 'w') as file:
	file.write('Hello World!')


print('-' * 20)

@contextmanager
def my_open(caminho_arquivo, modo):
	try:
		print('Abrindo arquivo')
		arquivo = open(caminho_arquivo, modo, encoding='utf8')
		yield arquivo # Generator
	except Exception as e:
		print('Ocorreu um erro',str(e))
	finally:
		print('Fechando arquivo')
		arquivo.close()



with my_open('teste.txt', 'w') as file:
	file.write('Hello world!')

