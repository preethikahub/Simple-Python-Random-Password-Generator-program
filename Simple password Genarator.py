import random
import string

# Function to generate password
def generate_password():

    print("===== RANDOM PASSWORD GENERATOR =====")

    
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Length must be greater than 0")
            else:
                break
        except ValueError:
            print("Please enter a valid number")

    print("\nSelect character types to include:")

    use_lower = input("Include lowercase letters? (yes/no): ").lower()
    use_upper = input("Include uppercase letters? (yes/no): ").lower()
    use_numbers = input("Include numbers? (yes/no): ").lower()
    use_symbols = input("Include symbols? (yes/no): ").lower()

    characters = ""

    
    if use_lower == "yes":
        characters += string.ascii_lowercase
        print("Lowercase letters added")

    
    if use_upper == "yes":
        characters += string.ascii_uppercase
        print("Uppercase letters added")

    
    if use_numbers == "yes":
        characters += string.digits
        print("Numbers added")

   
    if use_symbols == "yes":
        characters += string.punctuation
        print("Symbols added")

    
    if characters == "":
        print("\nError: No character type selected!")
        print("Please run the program again and select at least one option.")
        return

    
    password = ""

    for i in range(length):
        random_char = random.choice(characters)
        password += random_char

    
    print("\n===== GENERATED PASSWORD =====")
    print("Password:", password)
    print("Password Length:", len(password))
    print("Password Generated Successfully!")


def main():
    while True:
        generate_password()

        again = input("\nDo you want to generate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Password Generator!")
            break


main()