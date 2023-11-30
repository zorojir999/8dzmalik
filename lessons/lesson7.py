import sqlite3

op36_3_db = sqlite3.connect('op36_3.db')
cursor = op36_3_db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student(
name TEXT,
surname TEXT,
birth_year DATE,
hobby TEXT,
points INTEGER
)''')

# cursor.execute('''INSERT INTO student VALUES ('erwr', 'rereak', '1999-12-29', 'skiing', 11)''')
cursor.execute('''SELECT * FROM student WHERE LENGTH(surname) >=10''')
cursor.execute('''UPDATE student SET name = 'GENIUS' WHERE points >= 10''')
cursor.execute('''DELETE FROM STUDENT WHERE rowid % 2 ==0 ''')
cursor.execute('''SELECT * FROM student''')

results = cursor.fetchall()
for i in results:
    print(i)