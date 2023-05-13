import sqlite3

from main import DB_FILE

TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
cursor.execute(
	f'INSERT INTO {TABLE_NAME} (name, weight) '
	'VALUES '    
	'("Helena", 4), '
	'("Eduardo", 10)'
)
connection.commit()

# Evitando sql injection
sql = (
	f'INSERT INTO {TABLE_NAME} (name, weight) '
	'VALUES '    
	'(?, ?)'
)
cursor.execute(sql, ['Joana', 4])
connection.commit()

# Executar vários comandos
cursor.executemany(sql, (
	('Joana', 4), 
	('Luiz', 5),
))
connection.commit()

# Usando dicionários
sql = (
	f'INSERT INTO {TABLE_NAME} (name, weight) '
	'VALUES '    
	'(:nome, :peso)'
)
cursor.execute(sql, {
	'nome':'Joana',
	'peso': 20
})
connection.commit()

cursor.close()
connection.close()	