# SQL - язык структурированных запросов
# база данных -
# СУБД- система управления базами данных
# NOsql:SQL
# posgreSQL,mySQL, SQLite3-2

import sqlite3

# CRUD - create reed update delete
db = sqlite3.connect('op36_3.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE user(
lastname TEXT,
age INTEGER,
view INTEGER,
bitday DATE
)''')


db.close()