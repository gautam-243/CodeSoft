import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Make sure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the remaining password length with a random selection of all characters
    all_characters = lowercase + uppercase + digits + special_chars
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list back to a string and return it
    return ''.join(password)

# Get password length from the user
try:
    length = int(input("Enter the length of the password: "))
    generated_password = generate_password(length)
    if generated_password:
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number for the password length.")
