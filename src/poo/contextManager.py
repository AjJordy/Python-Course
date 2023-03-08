
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


 
with MyContextManager('./teste.txt', 'w') as file:
	file.write('Hello World!')

