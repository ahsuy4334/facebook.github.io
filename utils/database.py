import sqlite3

def create_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS hacksey(name text primary key, password text)')

    connection.commit()
    connection.close()

def add_user(name, password):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO hacksey VALUES("{name}", "{password}")')

    connection.commit()
    connection.close()

def query_all():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM hacksey')
    query = [{'name': row[0], 'password': row[1]} for row in cursor.fetchall()]

    connection.close()

    return query