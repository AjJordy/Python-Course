# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# > pip install pymysql
# > pip install types-pymysql
# > pip install python-dotenv

import os

import dotenv
import pymysql

dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
	host=os.environ['MYSQL_HOST'],
	user=os.environ['MYSQL_USER'],
	passwd=os.environ['MYSQL_PASSWORD'],
	database=os.environ['MYSQL_DATABASE'],
)


def create(connection):
	with connection.cursor() as cursor:
		cursor.execute(
			f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
			'id INT NOT NULL AUTO_INCREMENT, '
			'name VARCHAR(50) NOT NULL, '
			'age INT NOT NULL, '
			'PRIMARY KEY (id)'
			')'
		)
		# CUIDADO: Limpa a tabela
		cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') 
	connection.commit()



def insert(connection):
	with connection.cursor() as cursor:	
		# Tuple
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(name, age) VALUES (%s, %s) '
		)
		result = cursor.execute(sql, ("Luiz", 25))
		
		# Dict
		data = { 
			"name": "Maria", 
			"age": 30 
		}
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(name, age) VALUES (%(name)s, %(age)s) '
		)
		result = cursor.execute(sql, data)
	connection.commit()



def insertMany(connection):
	with connection.cursor() as cursor:	
		# Insert Tuple
		data_tuple = (
			("Luiz", 25),
			("Pedro", 13)
		)
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(name, age) VALUES (%s, %s) '
		)
		result = cursor.execute(sql, data_tuple)
		
		# Insert Dict
		data_dict = (
			{ "name": "Maria",  "age": 30  },
			{ "name": "João", "age": 15 },
			{ "name": "Lucas", "age": 42 },
		)
		sql = (
			f'INSERT INTO {TABLE_NAME} '
			'(name, age) VALUES (%(name)s, %(age)s) '
		)
		result = cursor.executemany(sql, data_dict)
	connection.commit()
		


def read(connection):
	with connection.cursor() as cursor:	
		sql = (
			f'SELECT * FROM {TABLE_NAME} '
		)
		cursor.execute(sql)
		# data = cursor.fetchone()
		data = cursor.fetchall()
		for row in data:
			print(row)
		


with connection:	
	create(connection)		
	insert(connection)
	insertMany(connection)
	read(connection)
