import sqlite3


connection = sqlite3.connect("notes.db", check_same_thread=False)
cursor = connection.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        name STR, 
        note STR
        )""")
    connection.commit()
    
    
def add(name, note):
    cursor.execute("""INSERT INTO notes(
        name,
        note
        ) VALUES(?,?)""", (name, note))
    connection.commit()
    
    
def get_all():
    cursor.execute("""SELECT * FROM notes""")
    inf = cursor.fetchall()
    return inf


def delete_note(id):
    cursor.execute("""DELETE FROM notes WHERE id = ?""", (id,))
    connection.commit()
    
    
def change_note(id, name, note):
    cursor.execute("""UPDATE notes SET name = ?, note = ? WHERE id = ?""", (name, note, id))
    connection.commit()
    
    
def get_note(id):
    cursor.execute("""SELECT * FROM notes WHERE id = ?""", (id,))
    inf = cursor.fetchone()
    return inf


create_table()

