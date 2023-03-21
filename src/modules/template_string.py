import locale
import string
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')


texto = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa}, 
"""

def converte_para_brl(numero: float) -> str:
	brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
	return brl


data = datetime(2023, 3, 21)
dados = dict(
	nome='João',
	valor=converte_para_brl(1_234_456), # == 123456
	data=data.strftime('%d/%m/%Y'),
	empresa='O.M.',
	telefone='+55 (11) 7890-5432'
)


import json

print(json.dumps(dados, indent=2, ensure_ascii=False))

print('-'*10, 'Texto resultado', '-'*10)

template = string.Template(texto)
print(template.substitute(dados)) # safe_substitute
