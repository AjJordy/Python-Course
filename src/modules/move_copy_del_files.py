import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
print(HOME)
print(DESKTOP)

os.makedirs(ORIGINAL, exist_ok=True)
os.makedirs(NOVA_PASTA, exist_ok=True)


# ----------------- Copy ------------------------
# for root, dirs, files in os.walk(ORIGINAL):
# 	for dir_ in dirs:
# 		caminho_novo_dir = os.path.join(
# 			root.replace(ORIGINAL, NOVA_PASTA), dir_
# 		)
# 		print(caminho_novo_dir)
# 		os.makedirs(caminho_novo_dir, exist_ok=True)
# 	for file in files:
# 		caminho_arquivo = os.path.join(root, file)
# 		print(caminho_arquivo)
# 		caminho_novo_arquivo = os.path.join(
# 			root.replace(ORIGINAL, NOVA_PASTA), 
# 			file
# 		)
# 		shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# ----------------- Copy easy way ------------------------

# os.unlink(NOVA_PASTA)	# Não apaga recursivamente
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA+'_2')

# Apagar arquivos   -> os.unlink
# Renomear ou mover -> shutil.move ou os.rename