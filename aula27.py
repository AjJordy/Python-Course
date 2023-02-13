"""
Fatiamento de strings
[i:f:p] [::]
i - inicio
f - fim
p - passo
Obs.: A função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel)
print('Posição 5:', variavel[5])
print('Posição -4:',variavel[-4])
print('Do 4 ao fim:',variavel[4:]) 
print('Do 4 ao 7:',variavel[4:8]) 
print('Do 1 ao 7 de 2 em 2:',variavel[1:8:2]) 
print('Invertida:',variavel[::-1])
print('Tamanho:',len(variavel))