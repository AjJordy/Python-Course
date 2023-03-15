import os

# ------------------ system ----------------------------
os.system('cls')
os.system('echo "Hello World"')


# ------------------ path ----------------------------
caminho = os.path.join('home','user','Desktop','curso','arquivo.txt')
print('caminho:', caminho)

diretorio, arquivo = os.path.split(caminho)
print('arquivo:', arquivo)

nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print('nome_arquivo:', nome_arquivo, 'extensao_arquivo:', extensao_arquivo)

caminho_existe = os.path.exists(caminho)
print('caminho_existe:', caminho_existe) 

absoluto = os.path.abspath('.')
print('absoluto:', absoluto)

base_name = os.path.basename(caminho)
print('base_name:', base_name)

dir_name = os.path.dirname(caminho)
print('dir_name:', dir_name)

path = os.path.join(absoluto, 'src')
print("Listando arquivos em ", path)
for pasta in os.listdir(path):
	full_path = os.path.join(path, pasta)
	print(pasta)
	if not os.path.isdir(full_path):		
		continue

	for file in os.listdir(full_path):
		print('  ',file)


# ------------------ walk ----------------------------
for root, dirs, files in os.walk(path):
	print('root:',root)

	for dir_ in dirs:
		print('  dir:', dir_)

	for file_ in files:
		print('  file:', file_)

