# Decoradores com parâmetros
# multiplica resultado
def decorator_with_func(multiplier):
	print('decorator_with_params')
	def decorator(func):
		print('decorator')
		def inner(*args, **kwargs):
			print('inner')			
			res = func(*args, **kwargs) * multiplier
			print(f'valor * {multiplier} = {res}' )
			
			return res
		return inner
	return decorator


@decorator_with_func(3)
@decorator_with_func(2) 
def soma(x, y):
	print(f"{x} + {y}")
	return x + y


print("Resultado:", soma(1, 2) )
