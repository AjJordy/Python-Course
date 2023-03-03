""" Hard way """
# Decorator function
# def create_function(func):
# 	def intern(*args, **kwargs):
# 		for arg in args:
# 			is_string(arg)
# 		result = func(*args, **kwargs)
# 		return result
# 	return intern

# def invert_string(string):
# 	return string[::-1]

# def is_string(param):
# 	if not isinstance(param, str):
# 		raise TypeError

# invert_string_check_param = create_function(invert_string)
# invertida = invert_string_check_param('hello')
# print(invertida)


""" Easy way """
# Syntax sugar
def create_function(func):
	def intern(*args, **kwargs):
		for arg in args:
			is_string(arg)
		result = func(*args, **kwargs)
		return result
	return intern


def is_string(param):
	if not isinstance(param, str):
		raise TypeError


@create_function
def invert_string(string):
	return string[::-1]
