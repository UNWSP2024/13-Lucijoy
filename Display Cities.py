import sqlite3
import os
print(f"Current working directory: {os.getcwd()}")
db_path = 'cities.db'

if os.path.exists(db_path):
    print(f"Found {db_path} in the current directory!")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cities")
        rows = cursor.fetchall()

        print("\nData from Cities table:")
        for row in rows:
            print(f"CityID: {row[0]}, CityName: {row[1]}, Population: {row[2]}")

        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while accessing the database: {e}")
else:
    print(f"{db_path} NOT found in the current directory!")