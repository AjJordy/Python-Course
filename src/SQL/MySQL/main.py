# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
# > pip install types-pymysql
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    passwd='senhas',
    database='base_de_dados',
)


# cursor = connection.cursor()
with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)



# cursor.close()
# connection.close()