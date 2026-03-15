import random
import string

# Function to generate password
def generate_password():

    print("===== RANDOM PASSWORD GENERATOR =====")

    # Ask user for password length
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Length must be greater than 0")
            else:
                break
        except ValueError:
            print("Please enter a valid number")

    # Ask user which characters to include
    print("\nSelect character types to include:")

    use_lower = input("Include lowercase letters? (yes/no): ").lower()
    use_upper = input("Include uppercase letters? (yes/no): ").lower()
    use_numbers = input("Include numbers? (yes/no): ").lower()
    use_symbols = input("Include symbols? (yes/no): ").lower()

    characters = ""

    # Add lowercase letters
    if use_lower == "yes":
        characters += string.ascii_lowercase
        print("Lowercase letters added")

    # Add uppercase letters
    if use_upper == "yes":
        characters += string.ascii_uppercase
        print("Uppercase letters added")

    # Add digits
    if use_numbers == "yes":
        characters += string.digits
        print("Numbers added")

    # Add symbols
    if use_symbols == "yes":
        characters += string.punctuation
        print("Symbols added")

    # Check if at least one option selected
    if characters == "":
        print("\nError: No character type selected!")
        print("Please run the program again and select at least one option.")
        return

    # Generate password
    password = ""

    for i in range(length):
        random_char = random.choice(characters)
        password += random_char

    # Display result
    print("\n===== GENERATED PASSWORD =====")
    print("Password:", password)
    print("Password Length:", len(password))
    print("Password Generated Successfully!")

# Main program
def main():
    while True:
        generate_password()

        again = input("\nDo you want to generate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Password Generator!")
            break

# Run program
main()
