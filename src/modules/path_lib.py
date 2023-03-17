from pathlib import Path

# Caminho absoluto
caminho = Path()
print('relative:',caminho)
print('absolute:',caminho.absolute())

# Caminho pai
caminho_arquivo = Path(__file__)
print('file:', caminho_arquivo)
print('parent:', caminho_arquivo.parent)
print('parent of parent:', caminho_arquivo.parent.parent)

# Referencia ao Home
ideias = caminho_arquivo.parent / 'ideias'
print('new path:', ideias)
print('Home:', Path.home())
print('Desktop:', Path.home() / 'Desktop')


# Criando, escrevendo e deletando arquivo
arquivo = caminho.absolute() / 'arquivo.txt'
arquivo.touch() # cria arquivo 
arquivo.write_text('Hello World!')
print('file:',arquivo.read_text())
arquivo.unlink() # apaga arquivo


# Abrindo arquivo em append mode
with arquivo.open('a+') as file:
	file.write('uma linha\n')
	file.write('outra linha\n')
print(arquivo.read_text())
print('is file ?',arquivo.is_file())

# Criando pastas
pasta = caminho.absolute() / 'pasta_teste'
pasta.mkdir(exist_ok=True)
print('is dir ?', pasta.is_dir())

