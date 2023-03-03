
path_file = 'test.txt'

# Modes: 
# r (read), w (write), x (create)
# a (append), b (binary)
# t (text), + (read and write)

# ----- BAD WAY -----
# file = open(path_file, 'w')
# file.close()

# ----- BETTER WAY -----
# Write
with open(path_file, 'w') as file:
	file.write('Hello world!\n')

# Read	
with open(path_file, 'r') as file:
	print(file.read())


print('-' * 10)

# Read and write
with open(path_file, 'w+') as file:
	file.write('Hello world 2!\n')
	file.seek(0,0) # Return to begin of file
	print(file.read())