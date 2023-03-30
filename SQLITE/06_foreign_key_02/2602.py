import sqlite3

conn = sqlite3.connect("2602.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        street TEXT,
        city TEXT,
        state TEXT,
        credit_limit REAL
    )
""")

cur.execute("""
    INSERT INTO customers (name, street, city, state, credit_limit) VALUES
    ("Pedro Augusto da Rocha", "Rua Pedro Carlos Hoffman", "Porto Alegre", "RS", 700.00),
    ("Antonio Carlos Mamel", "Av. Pinheiros", "Belo Horizonte", "MG", 3500.00),
    ("Luiza Augusta Mhor", "Rua Salto Grande", "Niteroi", "RJ", 4000.00),
    ("Jane Ester", "Av 7 de satembro", "Erechim", "RS", 800.00),
    ("Marcos Antonio dos Santos", "Av Farrapos", "Porto Alegre", "RS", 4250.25);
""")

conn.commit()
conn.close()

    
