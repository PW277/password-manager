import sqlite3

#Main menu for CLI
def main_menu():
    print("\nWelcome to the password manager CLI.")
    print("--------------------------------------")
    print("1. Add a New Password.")
    print("2. View All Passwords.")
    print("3. Search for a Password.")
    print("4. Exit.")

#Code to add a password to the database
def add_password():
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    notes = input("Enter any additional optional notes: ")

    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO passwords (service, username, password, notes)
    VALUES (?,?,?,?)
    ''', (service, username, password, notes))
    conn.commit()
    conn.close()

    print(f"Password for {service} added successfuly!")

#Code to view currently stored passwords
def view_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, service, username FROM passwords")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\nStored Passwords: ")
        for row in rows:
            print(f"ID: {row[0]}, Service: {row[1]}, Username: {row[2]}")
    else:
        print("\nNo passwords stored yet")

def search_password():
    service = input("Enter the service name to search: ")

    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords WHERE service = ?", (service,))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"\nService: {row[1]}, Username: {row[2]}, Password: {row[3]}, Notes: {row[4]}")
    else:
        print(f"\nNo passwords found for {service}.")

def run():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    #Create the database and table if not already created
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        notes TEXT             
)
''')
    conn.commit()
    conn.close()
    run()
