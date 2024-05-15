import hashlib
import getpass
import json
import pyperclip

password_manager = {}

def create_account():
    username = input("Enter Desired Username: ")
    password = getpass.getpass("Enter Desired Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account Created Successfully.")

def login():
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login Successful.")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to Create An Account, 2 to Login, or 3 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Please input a valid option.")

if __name__ == "__main__":
    main()