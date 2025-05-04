# Author: Lucia Floan
# Date Written: 05/03/2025
# Program Title: Phone book data creation
import sqlite3

def create_phonebook_db():
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            PhoneNumber TEXT NOT NULL
        )
        ''')
        conn.commit()
        print("Phone book database and table created successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
if __name__ == "__main__":
    create_phonebook_db()