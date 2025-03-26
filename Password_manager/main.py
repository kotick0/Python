from cryptography.fernet import Fernet
import questionary as quest
import os
import sqlite3 as sql

# TODO: Change code layout for fernet encryption support
# TODO: Finish if statements
# TODO: Error handeling
# TODO: Make it cleaner

# Sql conncetion and cursor variables
con = sql.connect("passwords.db")
cursor = con.cursor()

# Create database if one does not exist
create_database = """CREATE TABLE IF NOT EXISTS
passwords(id INTEGER PRIMARY KEY, account TEXT, password TEXT, date_added TEXT DEFAULT (datetime('now', 'localtime')))"""
cursor.execute(create_database)

# Read file.key from file as byte data (without the b'')
with open(
    "pass.key",
    "rb",
) as key_file:
    key = key_file.read()

# Fernet key variable
f = Fernet(key)

# CLI specific
choice = quest.select(
    "Welcome to uwuPass",
    choices=[
        "Save a new password",
        "Retrieve a password",
        "Delete a password",
        "List all saved accounts",
        "Exit",
    ],
    qmark="->",
).ask()  # Returns value of selection
os.system("clear")

# User chocie if statements
if choice == "Save a new password":
    account = str(input("Please insert account name: "))
    password = str(input("Please insert password: "))
    cursor.execute(
        "INSERT INTO passwords (account, password) VALUES (?, ?)",
        (
            f"{account}",
            f"{password}",
        ),
    )
    cursor.execute("SELECT * FROM passwords")
    results = cursor.fetchall()
    print(results)
elif choice == "Retrieve a password":
    print("2")
elif choice == "Delete a password":
    print("3")
elif choice == "List all saved accounts":
    print("4")
else:
    exit()
