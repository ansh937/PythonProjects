from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Encrypting the password for security (making the password into random numbers and symbols) 

print("Welcome to the password manager")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        write_key()  # Create the key if it doesn't exist
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Function to derive a key from the starter password using PBKDF2 HMAC SHA256
def derive_key(password: str, salt: bytes) -> bytes:
    return base64.urlsafe_b64encode(
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# Ensure the key file exists before proceeding
key_file_content = load_key()

# Load the encryption key and derive a key from the starter password
starter_password = input("What is your starter password? ")
salt = key_file_content[:16]  # Using the first 16 bytes of the key as salt
key = derive_key(starter_password, salt)
fer = Fernet(key)

def view_password():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_pass = data.split("|")
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                print(f"userName: {user} | password: {decrypted_pass}")
    except FileNotFoundError:
        print("Password file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_password():
    name = input("What is your name? ")
    password = input("What is your password? ")
    encrypted_pass = fer.encrypt(password.encode()).decode()
    
    with open("password.txt", "a") as f:
        f.write(name + "|" + encrypted_pass + "\n")

while True:
    pwd = input("""
    Enter 1: TO view the existing password.
    Enter 2: to add new password.
    Enter "q": to quit the program. 
    > """).strip()

    if pwd == "1":
        view_password()
    elif pwd == "2":
        add_password()
    elif pwd.lower() == "q":
        break
    else:
        print("Please enter a valid input")
