import pyodbc

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

server = 'comptef:europe-west1:comptefgpt2024'  # e.g., 'localhost' or an IP address
database = 'gpt_data'  
username = 'gpt_write'  
password = '2U$+vt-FE2c<aK)'  
# Specifying the ODBC driver, server name, database, etc. directly
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establishing the connection
conn = pyodbc.connect(connection_string)

# Create a cursor from the connection
cursor = conn.cursor()

# Create table
if conn is not None:
    create_table(conn)
    conn.close()
else:
    print("Error! Cannot create the database connection.")
