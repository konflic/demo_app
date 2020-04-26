import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user

DB = 'db_storage/contacts.sqlite'
db = SQLAlchemy()


def create_table(table):
    connection = sqlite3.connect(DB)
    create_sql = """create TABLE IF NOT EXISTS {table_name}
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT DEFAULT NULL,
        phone TEXT NOT NULL,
        address TEXT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
    );""".format(table_name=table)
    connection.execute(create_sql)
    connection.close()


def connect():
    return sqlite3.connect(DB)


def insert_data(name, phone, email=None, address=None):
    conn = connect()
    sql = "INSERT INTO {table} (name, email, phone, address) VALUES (?, ?, ?, ?)".format(table=current_user.contacts)
    data = (name, email, phone, address)
    conn.execute(sql, data)
    conn.commit()
    conn.close()


def get_data():
    conn = connect()
    sql = "SELECT * FROM {table}".format(table=current_user.contacts)
    return conn.execute(sql).fetchall()


def remove_data(id):
    conn = connect()
    sql = "DELETE FROM {table} WHERE id = ?".format(table=current_user.contacts)
    conn.execute(sql, (id,))
    conn.commit()
    conn.close()
