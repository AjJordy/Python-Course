

class MyError(Exception):
	...

class OtherError(Exception):
	...

def levantar():
	exception_ = MyError('a','b','c')
	exception_.add_note('Olha a nota')
	raise exception_

try:
	levantar()
except MyError as error:
	print(error.args)
	exception_ = OtherError('Vou lancar outro erro')
	exception_.__notes__ = error.__notes__.copy()
	exception_.add_note('Mais uma nota') 
	raise exception_