import random
import string

print("========== ADVANCED RANDOM PASSWORD GENERATOR ==========")

# List to store password history
password_history = []

# Function to check password strength
def check_strength(password):
    if len(password) <= 6:
        return "Weak"
    elif len(password) <= 10:
        return "Medium"
    else:
        return "Strong"

# Function to generate password
def generate_password():

    # Ask password length
    length = int(input("Enter password length (minimum 6): "))

    if length < 6:
        print("Error: Password length must be at least 6")
        return

    # Ask number of passwords
    count = int(input("How many passwords do you want to generate?: "))

    # Ask user options
    print("\nSelect character types:")
    lower = input("Include lowercase letters? (yes/no): ")
    upper = input("Include uppercase letters? (yes/no): ")
    numbers = input("Include numbers? (yes/no): ")
    symbols = input("Include symbols? (yes/no): ")

    characters = ""

    # Add lowercase
    if lower.lower() == "yes":
        characters += string.ascii_lowercase
        print("Lowercase letters added")

    # Add uppercase
    if upper.lower() == "yes":
        characters += string.ascii_uppercase
        print("Uppercase letters added")

    # Add numbers
    if numbers.lower() == "yes":
        characters += string.digits
        print("Numbers added")

    # Add symbols
    if symbols.lower() == "yes":
        characters += string.punctuation
        print("Symbols added")

    # Check if user selected any option
    if characters == "":
        print("Error: No character type selected!")
        return

    print("\n========== GENERATED PASSWORDS ==========")

    for n in range(count):

        password = ""

        # Generate password
        for i in range(length):
            password += random.choice(characters)

        # Shuffle password for extra randomness
        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        # Save to history
        password_history.append(password)

        # Check strength
        strength = check_strength(password)

        print(f"Password {n+1}: {password}")
        print("Length:", len(password))
        print("Strength:", strength)
        print("----------------------------")

        # Save password to file
        save = input("Save this password to file? (yes/no): ")

        if save.lower() == "yes":
            file = open("passwords.txt", "a")
            file.write(password + "\n")
            file.close()
            print("Password saved to passwords.txt")

# Main program
while True:

    generate_password()

    print("\nPassword History:")
    for p in password_history:
        print(p)

    choice = input("\nGenerate another password? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Advanced Password Generator!")
        break