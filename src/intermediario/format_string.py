"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0 >-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'Numero na direito: {variavel: >10}.')
print(f'Numero na esquerda: {variavel: <10}.')
print(f'Numero no meio: {variavel: ^10}.')
print(f'Numero float: {1000.846518685484:0=+10,.1f}')
print(f'HEXA: {1500:08X}')