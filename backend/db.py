import sqlite3
from datetime import datetime

DB = "emergency_logs.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            query TEXT,
            category TEXT,
            method TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_event(query, category, method):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO logs VALUES (NULL, ?, ?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), query, category, method)
    )
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    rows = c.execute("SELECT * FROM logs ORDER BY id DESC").fetchall()
    conn.close()
    return rows
