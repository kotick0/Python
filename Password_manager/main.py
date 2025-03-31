from cryptography.fernet import Fernet
from tabulate import tabulate
import questionary as quest
import os
import sqlite3 as sql
import time

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
    print("Key file not found. Generating key...")
    time.sleep(0.6)
    os.system("cls" if os.name == "nt" else "clear")
    with open(
        "pass.key",
        "wb",
    ) as key_file:
        key_bytes = Fernet.generate_key()
        key_file.write(key_bytes)
        key = key_bytes

# Variable for storing Fernet key
f = Fernet(key)


# Functions for ease of writing
def clear():
    """OS clear terminal function"""
    os.system("cls" if os.name == "nt" else "clear")


def back_to_main_menu():
    """Go back to main menu prompt"""
    if quest.confirm("Do you wish to go back to main menu?").ask() == False:
        exit()


def account_menu():
    """Account choice menu"""
    cursor.execute("SELECT account FROM passwords")
    id_account = cursor.fetchall()
    account_chocies = [row[0] for row in id_account]
    try:
        choice = quest.select(
            "Please choose the account:", choices=account_chocies
        ).ask()
        return choice
    except Exception as e:
        print(f"Error: {e}")
        back_to_main_menu()


# Main menu and choices functions
def main_menu():
    """Main menu dispaly function"""
    try:
        while True:
            choice = quest.select(
                "Welcome to uwuPass",
                choices=[
                    "Save a new password",
                    "Retrieve account information",
                    "Delete a password",
                    "List all saved accounts",
                    "Exit",
                ],
                qmark="->",
            ).ask()  # Returns value of selection

            # User chocie if statements
            if choice == "Save a new password":
                clear()
                save_password()
            elif choice == "Retrieve account information":
                clear()
                retrieve_info()
            elif choice == "Delete a password":
                clear()
                delete_password()
            elif choice == "List all saved accounts":
                clear()
                list_accounts()
            else:
                break
    except KeyboardInterrupt:
        exit()


def save_password():
    """Saves encrpyed username password and password in the sqlite database"""
    try:
        account = quest.text("Please input the website/application name:").ask()
        username = quest.text("Please input the username:").ask()
        password = quest.password("Please input the pasword:").ask()

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
        clear()
        print(f"Account details for {account} saved!")
        time.sleep(0.8)
        back_to_main_menu()
        clear()
    except (KeyboardInterrupt, Exception):
        back_to_main_menu()
        clear()


def retrieve_info():
    """Asks user for account to fetch info from and retrieves username and password"""
    account_chocie = account_menu()
    clear()
    try:
        cursor.execute("SELECT * FROM passwords WHERE account = ?", (account_chocie,))
        account_temp = cursor.fetchone()
        username_decrypted = f.decrypt(account_temp[2]).decode("utf-8")
        password_decrypted = f.decrypt(account_temp[3]).decode("utf-8")
        quest.print(
            f"Username: {username_decrypted}\nPassword: {password_decrypted}",
            style="bold fg: pink",
        )
        time.sleep(0.8)
        back_to_main_menu()
        clear()
    except Exception as e:
        clear()


def delete_password():
    """Displays account list and deletes password for selected account"""
    deletion_choice = account_menu()
    clear()
    cursor.execute("DELETE FROM passwords WHERE account = ?", (deletion_choice,))
    con.commit()
    if deletion_choice != None:
        print(f"Account details for {deletion_choice} deleted!")
        time.sleep(0.8)
        back_to_main_menu()
        clear()


def list_accounts():
    """Lists all accounts saved in the sql database"""
    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    account_list = []
    for row in rows:
        id = row[0]
        account = row[1]
        username = f.decrypt(row[2]).decode("utf-8")
        password = f.decrypt(row[3]).decode("utf-8")
        time_stamp = row[4]
        account_list.append([id, account, username, password, time_stamp])
    tabulate_format = account_list
    headers = ["ID", "Account", "Username", "Password", "Time_stamp"]
    if account_list != []:
        print(tabulate(tabulate_format, headers=headers, tablefmt="grid"))
        time.sleep(0.8)
        back_to_main_menu()
        clear()
    else:
        print("No accounts currently saved!")
        time.sleep(0.8)
        clear()


# Calling main menu function for the program start
main_menu()
