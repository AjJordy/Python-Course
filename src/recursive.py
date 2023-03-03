# Função recursiva é uma função que ela sé chama de volta
def recursive(begin=0, end=10):
	if begin >= end:
		return end
	print(begin, end)
	begin += 1
	return recursive(begin, end)

print(recursive())


# Fatorial
def factorial(n):
	if n <= 1:
		return 1
	
	return n * factorial(n - 1)

print('Fatorial de 5:',factorial(5))
