import sqlite3

conn = sqlite3.connect("expense.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    type TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

conn.commit()

# ---------- AUTH ----------
def register_user(u, p):
    cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (u,p))
    conn.commit()

def login_user(u, p):
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p))
    return cur.fetchone()

# ---------- EXPENSE ----------
def add_expense(data):
    cur.execute("""
        INSERT INTO expenses (date,type,category,amount,description)
        VALUES (?,?,?,?,?)
    """, data)
    conn.commit()

def fetch_all():
    cur.execute("SELECT * FROM expenses")
    return cur.fetchall()

def delete_one(id):
    cur.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()

def update_expense(id, amount):
    cur.execute("UPDATE expenses SET amount=? WHERE id=?", (amount,id))
    conn.commit()

def search(keyword):
    cur.execute("SELECT * FROM expenses WHERE category LIKE ?", ('%'+keyword+'%',))
    return cur.fetchall()

def summary():
    cur.execute("SELECT type, SUM(amount) FROM expenses GROUP BY type")
    return cur.fetchall()

def category_data():
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    return cur.fetchall()