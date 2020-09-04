import hashlib
from Encryptor import Encryptor


def get_email_and_password():
    """
    Asks for the users email and password
    """
    password = input("What is your password?\n\n* ")
    print()

    email = input("What is your email?\n\n* ")
    print()
    return email, password


def generate_key(password, salt):
    """
    Generates a key based on a password and a salt input
    """
    if(type(password) != type(b"")):
        password = str.encode(password)

    if(type(salt) != type(b"")):
        salt = str.encode(salt)

    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return dk


email, password = get_email_and_password()

first_key = generate_key(password, email)
second_key = generate_key(first_key.hex(), email)

print('Key 1: ', first_key)
print('Key 2: ', second_key)
