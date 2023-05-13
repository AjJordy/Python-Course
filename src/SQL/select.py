import sqlite3

from main import DB_FILE

TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = f'SELECT * FROM {TABLE_NAME}'

print('---- fethall ----')
cursor.execute(sql)
for row in cursor.fetchall():
    # _id, name, weight = row
    print(*row)
    
print('---- fethone ----')
cursor.execute(sql)
row = cursor.fetchone()
print(*row)

print('---- WHERE ----')
cursor.execute(f'{sql} WHERE id ="3"')
row = cursor.fetchone()
print(*row)


cursor.close()
connection.close()	