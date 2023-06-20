import requests


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome 
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://teste.com')
        if resposta.ok:
            return 'CONECTADO'        
        return 'ERRO 404'