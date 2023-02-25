"""
Aula 29
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que vc digitar: ')
try:
	numero_float = float(numero_str)
	print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except Exception as e:
	print('Erro:',str(e))
