import sqlite3

from main import DB_FILE

TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
	f'DELETE FROM {TABLE_NAME} '
    'WHERE id = 3'
)
connection.commit()

cursor.execute(
	f'SELECT * FROM {TABLE_NAME}'
)
for row in cursor.fetchall():    
    print(*row)

cursor.close()
connection.close()	