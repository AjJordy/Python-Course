# Variáveis de ambiente no Sistema operacional
# Linux:   $ export SENHA='minhaSenha' 
# Windows: > $env:SENHA="minhaSenha"


import os

# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

load_dotenv()

# print(os.environ)
print(os.getenv('DB_USER'))
print(os.getenv('DB_PORT'))
print(os.getenv('DB_HOST'))

