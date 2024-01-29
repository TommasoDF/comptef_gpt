import sqlite3
from datetime import datetime

# Function to create a connection to the database
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# Function to create the table
def create_table(conn):
    """ Create a table """
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS user_interactions (
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                  matriculation_number TEXT NOT NULL,
                                  user_question TEXT NOT NULL,
                                  gpt_answer TEXT NOT NULL
                              );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
    except Error as e:
        print(e)

# Path to your database file
database = "app.db"

# Create a database connection
conn = create_connection(database)

# Create table
if conn is not None:
    create_table(conn)
    conn.close()
else:
    print("Error! Cannot create the database connection.")
