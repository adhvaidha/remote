# Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

# Stored credentials (example)
stored_username = "admin"
stored_password = "1234"

if username == stored_username and password == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password")
