import os
import getpass
from banner import display_banner
from auth import register, login
from database import create_users_table

def main_menu():
    while True:
        print("\n\n\n1. Register")
        print("2. Login\n")
        choice = input("Choose an option (1/2): ")
        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if login(username, password):
                print(f"\033[91mLogged in as {username}\033[0m")
                break
            else:
                print("Invalid username or password")

if __name__ == "__main__":
    create_users_table()
    display_banner()
    main_menu()
