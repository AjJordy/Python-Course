import sys

# Generator expression
print('--------- Generator expression ---------')
generator = (n for n in range(10000))

print(generator)
print(sys.getsizeof(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Generator function
print('--------- Generator function ---------')
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


# Generator with generators 
print('--------- Generator with generators ---------')
def gen1():
	yield 1
	yield 2
	yield 3

def gen2():
	yield from gen1()
	yield 4
	yield 5
	yield 6

g = gen2()
for num in g:
	print(num)