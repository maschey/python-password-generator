import secrets
import string
import random

password_scaffolding = string.ascii_letters + string.digits + string.punctuation
def get_length():
    length = int(input("Length of Password (default 12): ") or "12")
    return int(length)


def password_generator(length):
    password_scaffolding_list = list(password_scaffolding)

    return ''.join(secrets.choice(password_scaffolding_list) for i in range(length))


def main():
    print("This will generate a Password with special characters, numbers and letters. \n\n")
    length = get_length()
    print(password_generator(length))


if __name__ == '__main__':
    main()
