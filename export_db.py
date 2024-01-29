import sqlite3
import csv

def export_to_csv(db_file, csv_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Query the data
    cursor.execute("SELECT * FROM user_interactions")  # Replace with your table name
    data = cursor.fetchall()

    # Write data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow([i[0] for i in cursor.description])  # column headers
        # Write the data
        writer.writerows(data)

    # Close the connection
    conn.close()

# Path to your SQLite database
database = "app.db"

# Path to the CSV file you want to create
csv_output = "output.csv"

# Export to CSV
export_to_csv(database, csv_output)
