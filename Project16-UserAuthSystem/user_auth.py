import hashlib
import os
import getpass

USER_DB = "users.db"

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def user_exists(username):
    if not os.path.exists(USER_DB):
        return False
    with open(USER_DB, 'r') as f:
        for line in f:
            stored_user, _ = line.strip().split(":", 1)
            if username == stored_user:
                return True
    return False

def register_user(username, password):
    if user_exists(username):
        print(f"Username '{username}' already exists.")
        return False
    hashed = hash_password(password)
    with open(USER_DB, 'a') as f:
        f.write(f"{username}:{hashed}\n")
    print(f"User '{username}' registered successfully.")
    return True

def authenticate_user(username, password):
    hashed = hash_password(password)
    if not os.path.exists(USER_DB):
        print("No user database found.")
        return False

    with open(USER_DB, 'r') as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(":", 1)
            if username == stored_user and hashed == stored_hash:
                print("Authentication successful.")
                return True
    print("Authentication failed.")
    return False

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            u = input("Enter username: ").strip()
            p = getpass.getpass("Enter password: ")
            register_user(u, p)

        elif choice == "2":
            u = input("Enter username: ").strip()
            p = getpass.getpass("Enter password: ")
            authenticate_user(u, p)

        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
