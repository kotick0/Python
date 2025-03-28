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

# Create table in sql if one does not exist
create_database = """CREATE TABLE IF NOT EXISTS
passwords(id INTEGER PRIMARY KEY, account TEXT, username TEXT, password TEXT, date_added TEXT DEFAULT (datetime('now', 'localtime')))"""
cursor.execute(create_database)

# Create key file if one does not exist and read pass.key from file as byte data
try:
    with open(
        "pass.key",
        "rb",
    ) as key_file:
        key = key_file.read()
except FileNotFoundError:
    with open(
        "pass.key",
        "wb",
    ) as key_file:
        key_bytes = Fernet.generate_key()
        key_file.write(key_bytes)
        key = key_bytes

# Variable for storing Fernet key
f = Fernet(key)


# CLI main menu function
def main_menu():
    """Main menu dispaly function"""
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
    return choice


# CLI account choice menu
def account_menu():
    """Account choice menu"""
    cursor.execute("SELECT account FROM passwords")
    id_account = cursor.fetchall()
    account_chocies = [row[0] for row in id_account]
    print(id_account)
    choice = quest.select(
        "Please choose the account to fetch info from:", choices=account_chocies
    ).ask()
    return choice


main_choice = main_menu()
os.system("cls" if os.name == "nt" else "clear")

# User chocie if statements
if main_choice == "Save a new password":
    account = quest.text("Please input the website/application name:").ask()
    username = quest.text("Please input the username:").ask()
    password = quest.password("Please input the pasword:").ask()

    # Encrypt account details
    username_encrypted = f.encrypt(username.encode())
    password_encrypted = f.encrypt(password.encode())

    cursor.execute(
        "INSERT INTO passwords (account, username, password) VALUES (?, ?, ?)",
        (
            account,
            username_encrypted,
            password_encrypted,
        ),
    )
    con.commit()
    print("Account details saved!")
    exit()

elif main_choice == "Retrieve a password":
    account_chocie = account_menu()
    cursor.execute("SELECT * FROM passwords WHERE account = ?", (account_chocie,))
    account_data = cursor.fetchone()
    username_decrypted = f.decrypt(account_data[2]).decode("utf-8")
    password_decrypted = f.decrypt(account_data[3]).decode("utf-8")
    quest.print(
        f"Username: {username_decrypted}\nPassword: {password_decrypted}",
        style="bold fg: pink",
    )
elif main_choice == "Delete a password":
    print("3")
elif main_choice == "List all saved accounts":
    print("4")
else:
    exit()
