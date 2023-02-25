import sys

# Generator expression
generator = (n for n in range(10000))

print(generator)
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Generator function
def generator_func(n=0, maximun=10):
	while True:
		yield n 
		n += 1
		if n >= maximun:
			return # StopIteration Exception
		

gen = generator_func()
print(gen.__iter__())
# print(next(gen))
# print(next(gen))
# 		or 
for n in gen:
	print(n)