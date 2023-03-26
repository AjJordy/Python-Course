import sys

argumentos = sys.argv
qtd_args = len(argumentos)

if qtd_args <= 1:
	print('Você não passou argumentos')
else:
	try:
		print(f'Você passou os argumetnos {argumentos[1:]}')
		print(f'Faça  {argumentos[1]}')
	except IndexError:
		print('Faltam argumentos')


# Argument Parser
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b', '--basic', 
	help='Mostra "Olá mundo na tela',
	type=str,
	metavar='STRING',
	default='Olá mundo',
	required=False,
	action='append', # Recebe o argumento mais de uma vez
	# nargs='+', # Recebe mais de um valor
)

parser.add_argument('-v', '--verbose', 
	help='Mostra logs',
	action='store_true',
)

args = parser.parse_args()

if args.basic is None:
	print(args.basic)
else: 
	print('Voce não passou o argumento -b ou --basic')