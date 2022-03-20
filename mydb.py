import sqlite3

conn = sqlite3.connect('database/signup.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS sign(id integer primary key,email string(100),pasw string(30),pas_repeat string(30))')
    conn.commit()
    c.close()
    conn.close()

create_table()
