import secrets
import string

print('Random number below value:', secrets.randbelow(100))


random = secrets.SystemRandom()

values = string.ascii_letters + string.digits + string.punctuation
print('values:', values)

password = ''.join(random.choices(values, k=32))
print('password:', password)

# r_range = random.randrange(10, 20)
# print('Random number between 10 and 20:', r_range)

# r_even = random.randrange(10, 20, 2)
# print('Random number between 10 and 20 but evens:', r_even)

# r_int = random.randint(10, 20)
# print('Random int between 10 and 20:', r_int)

# r_float = random.uniform(10, 20)
# print('Random float between 10 and 20:', r_float)

# names = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(names)
# print('Shuffle list:', names)

# new_names = random.sample(names, k=len(names))
# print('New list shuffled:', new_names)

# new_choices = random.choices(names, k=len(names))
# print('New list (can repeat):', new_choices)

# choice = random.choice(names)
# print('Choice a random item:', choice)
