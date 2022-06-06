import random as rd
import string as str


def generate_password():
    characters = str.ascii_lowercase + str.digits + str.punctuation + str.ascii_uppercase
    password = []

    for i in range(15):
        random_char = rd.choice(characters)
        password.append(random_char)

    password = "".join(password)
    return password


def main():
    password = generate_password()
    print("Your new password is: " + password)


if __name__ == "__main__":
    main()