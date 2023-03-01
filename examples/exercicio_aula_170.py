"""
Some os valores nas listas retornando uma nova lsita com os valores somados
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor
"""

lista_a = [1,2,3,4,5,6]
lista_b = [1,2,3,4]

lista_soma = [ x + y for x, y in zip(lista_a, lista_b) ]
print(lista_soma)