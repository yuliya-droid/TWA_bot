CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    available_kayaks INTEGER NOT NULL
);
