import random
import string

print("========== RANDOM PASSWORD GENERATOR ==========")

# Function to generate password
def generate_password():

    # Ask password length
    length = int(input("Enter password length: "))

    # Ask user options
    print("\nSelect character types:")
    lower = input("Include lowercase letters? (yes/no): ")
    upper = input("Include uppercase letters? (yes/no): ")
    numbers = input("Include numbers? (yes/no): ")
    symbols = input("Include symbols? (yes/no): ")

    characters = ""

    # Add lowercase letters
    if lower == "yes":
        characters += string.ascii_lowercase
        print("Lowercase letters added")

    # Add uppercase letters
    if upper == "yes":
        characters += string.ascii_uppercase
        print("Uppercase letters added")

    # Add numbers
    if numbers == "yes":
        characters += string.digits
        print("Numbers added")

    # Add symbols
    if symbols == "yes":
        characters += string.punctuation
        print("Symbols added")

    # Check if any option selected
    if characters == "":
        print("Error: No character type selected!")
        return

    # Generate password
    password = ""

    for i in range(length):
        random_char = random.choice(characters)
        password += random_char

    # Display result
    print("\nGenerated Password:", password)
    print("Password Length:", len(password))
    print("Password generated successfully!")

# Run program
while True:
    generate_password()

    choice = input("\nGenerate another password? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the program!")
        break
