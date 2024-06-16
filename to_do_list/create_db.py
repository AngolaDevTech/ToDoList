import sqlite3

def create_db():
    conn = sqlite3.connect('to_do_list.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        is_completed INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
