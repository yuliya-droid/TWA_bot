import sqlite3

def initialize_db():
    conn = sqlite3.connect('kayak_reservations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    available_kayaks INTEGER NOT NULL
                 )''')
    # Пример добавления записей
    c.execute("INSERT INTO reservations (date, time, available_kayaks) VALUES ('2024-07-12', '14:00', 5)")
    c.execute("INSERT INTO reservations (date, time, available_kayaks) VALUES ('2024-07-13', '10:00', 3)")
    conn.commit()
    conn.close()

initialize_db()
