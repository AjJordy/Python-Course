import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


if __name__ == '__main__':

	connection = sqlite3.connect(DB_FILE)
	cursor = connection.cursor()

	# CUIDADO: fazendo o delete sem where
	cursor.execute(
		f'DELETE FROM {TABLE_NAME}'
	)
	cursor.execute(
		f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
	)
	connection.commit()

	# Criar a tabela
	cursor.execute(
		f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
		'('
		'id INTEGER PRIMARY KEY AUTOINCREMENT,'
		'name TEXT,'
		'weight REAL'
		')'
	)
	connection.commit()

	cursor.close()
	connection.close()