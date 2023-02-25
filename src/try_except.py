"""
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

try:
	a = 18
	b = 0
	c = a / b

except ZeroDivisionError: 
	print('Zero division Error')

except NameError:
	print('Name Error not found')

except Exception as error:
	print('Error unknow:',error)

else:
	print('Without error')

finally:
	print('Finish')


# Create my own Exception
print('----- Create my own Exception -----')
raise ValueError('My error')