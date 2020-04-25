import sqlite3
from flask_sqlalchemy import SQLAlchemy

DB = 'contacts.sqlite'
db = SQLAlchemy()


def crate_table():
    connection = sqlite3.connect(DB)
    create_sql = """create TABLE IF NOT EXISTS contacts
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT DEFAULT NULL,
        phone TEXT NOT NULL,
        address TEXT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );"""
    connection.execute(create_sql)
    connection.close()


def connect():
    return sqlite3.connect(DB)


def insert_data(name, phone, email=None, address=None):
    conn = connect()
    sql = "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)"
    data = (name, email, phone, address)
    conn.execute(sql, data)
    conn.commit()
    conn.close()


def get_data():
    conn = connect()
    sql = "SELECT * FROM contacts"
    return conn.execute(sql).fetchall()


def remove_data(id):
    conn = connect()
    sql = "DELETE FROM contacts WHERE id = ?"
    conn.execute(sql, (id,))
    conn.commit()
    conn.close()
