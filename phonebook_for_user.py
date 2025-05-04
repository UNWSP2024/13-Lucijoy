# Author: Lucia Floan
# Date Written: 05/03/2025
# Program Title: phonebook_for_user
import sqlite3

def lookup_entry():
    name = input("Enter the name to look up: ")
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT PhoneNumber FROM Entries WHERE Name=?", (name,))
    result = cursor.fetchone()
    if result:
        print(f"Phone number for {name}: {result[0]}")
    else:
        print("Name not found.")
    conn.close()

def update_entry():
    name = input("Enter the name to update: ")
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Entries WHERE Name=?", (name,))
    result = cursor.fetchone()
    if result:
        new_phone = input("Enter the new phone number: ")
        cursor.execute("UPDATE Entries SET PhoneNumber=? WHERE Name=?", (new_phone, name))
        conn.commit()
        print("Phone number updated.")
    else:
        print("Name not found.")
    conn.close()

def delete_entry():
    name = input("Enter the name to delete: ")
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Entries WHERE Name=?", (name,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM Entries WHERE Name=?", (name,))
        conn.commit()
        print("Entry deleted.")
    else:
        print("Name not found.")
    conn.close()

def main():
    while True:
        print("\n1. Look up a phone number")
        print("2. Update a phone number")
        print("3. Delete an entry")
        print("4. Exit")
        choice = input("Enter a choice 1-4): ")

        if choice == '1':
            lookup_entry()
        elif choice == '2':
            update_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid. Try again.")
if __name__ == "__main__":
    main()