from calculadora import soma

# print(soma(10, 20))

try:
    print(soma('15', 15))
except TypeError as e:
    print('Contra inválida')
    print(e)
