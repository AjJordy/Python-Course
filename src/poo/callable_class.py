

class CallMe:
	def __init__(self, phone) -> None:
		self.phone = phone 

	# Callable
	def __call__(self, *args, **kwds):
		print('Chamando, ', self.phone)
		return self.phone


call1 = CallMe('123456789')
ret = call1()
print('retorno:', ret)