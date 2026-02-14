from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Ensure key file exists
if not os.path.exists("key.key"):
    write_key()

# Master password (currently not used – you can extend later)
master_pwd = input("What is the master password? ")   # stored but unused in this simple version

# Load the actual encryption key
key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data:
                continue
            user, passw = data.split("|")
            try:
                decrypted = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted)
            except:
                print(f"Error decrypting entry for {user}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        encrypted = fer.encrypt(pwd.encode()).decode()   # fixed parentheses
        f.write(name + "|" + encrypted + "\n")
    print("Password added.")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, q to quit)? ").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")