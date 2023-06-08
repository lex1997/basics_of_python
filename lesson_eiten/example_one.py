import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'
db_is_new = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('СОздана новая БД')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        print('вставка первоначальных данных')
        conn.executescript('''
        insert into project (name, description, deadlene)
        values ('pymotv', 'Python module of the week', '01.11.2023')
        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '25.05.2023', 'pymotv')
        ''')
    else:
        print('БД уже существует')

conn.close()


"""
CREATE TABLE IF NOT EXIST users(
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT;
)
"""