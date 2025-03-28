import questionary as quest


def main_menu():
    while True:  # Keeps looping until the user selects "Exit"
        choice = quest.select(
            "Welcome to uwuPass",
            choices=[
                "Save a new password",
                "Retrieve a password",
                "Delete a password",
                "List all saved accounts",
                "Exit",
            ],
        ).ask()

        if choice == "Save a new password":
            save_password()
        elif choice == "Retrieve a password":
            retrieve_password()
        elif choice == "Delete a password":
            delete_password()
        elif choice == "List all saved accounts":
            list_accounts()
        elif choice == "Exit":
            print("Exiting program...")
            break  # Exits the loop and stops the program
        else:
            print("Invalid choice, please try again.")


def save_password():
    print("Saving password... (returning to main menu)")


def retrieve_password():
    print("Retrieving password... (returning to main menu)")


def delete_password():
    print("Deleting password... (returning to main menu)")


def list_accounts():
    print("Listing all saved accounts... (returning to main menu)")


# Run the main menu
main_menu()
