# https://docs.python.org/3/py-modindex.html

"""
Importa o modulo inteiro
 - Vantagem: Proteção do namespace 
 - Desvantagem: Nomes grandes
"""
import sys
print(sys.platform)

# Importa o modulo e renomeia
# - Não é muito recomendado
# import sys as s

"""
Importa parte do modulo
 - Vantagem: Nomes pequenos
 - Desvantagem: Sem o namespace do módulo
"""
from sys import platform
print(platform)


"""
Importar tudo do modulo
 => Má pratica
 - Vantagem: Importa tudo de um módulo
 - Desvantagem: Importa tudo de um módulo (sem namespace)
"""
from json import *
