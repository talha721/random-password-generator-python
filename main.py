import random
import string

print("Welcome to Python Random Password Generator")
password_length = int(input("Enter password length: "))

print("\nChoose the password complexity")
print("1. Simple")
print("2. Medium")
print("3. Strong")
password_complexity = int(input("Enter your choice (1, 2 or 3): "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_random_password():
    characters = ""
    if password_complexity == 1:
        characters = letters
    elif password_complexity == 2:
        characters = letters + digits
    elif password_complexity == 3:
        characters = letters + digits + symbols
    random_characters = ''.join(random.choice(characters) for i in range(password_length))
    return random_characters

random_string = generate_random_password()
print(f"Password: {random_string}")