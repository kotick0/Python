import sqlite3 as sql
import os

print(os.getcwd())
connection = sql.connect("passwords.db")
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
passwords(id INTEGER PRIMARY KEY, account TEXT, password TEXT, date_added TEXT DEFAULT (datetime('now', 'localtime')))"""

cursor.execute(command1)
# cursor.execute("INSERT INTO passwords VALUES (?, 'konto', 'haslo', '2025-03-26')")
account = str(input("Please insert account name: "))
password = str(input("Please insert password: "))
cursor.execute(
    "INSERT INTO passwords (account, password) VALUES (?, ?)",
    (f"{account}", f"{password}"),
)

cursor.execute("SELECT * FROM passwords")
results = cursor.fetchall()
print(results)
