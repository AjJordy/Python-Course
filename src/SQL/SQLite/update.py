import sqlite3

from main import DB_FILE

TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
	f'UPDATE {TABLE_NAME} '
    'SET name="Qualquer valor", weight=67.89 '
    'WHERE id = 1'
)
connection.commit()

cursor.execute(
	f'SELECT * FROM {TABLE_NAME}'
)
for row in cursor.fetchall():    
    print(*row)

cursor.close()
connection.close()	