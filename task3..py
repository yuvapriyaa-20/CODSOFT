import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lower + upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
def main():
    print("Password Generator!!")
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
            return
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
