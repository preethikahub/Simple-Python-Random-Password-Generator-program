🔐 Random Password Generator (Python)

This project is a Random Password Generator written in Python.
It allows users to create secure passwords by choosing different character types such as lowercase letters, uppercase letters, numbers, and symbols.

📌 Features

- User can choose password length
- Option to include:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Symbols
- Generates strong and random passwords
- Option to generate multiple passwords
- Displays password length after generation

🛠 Technologies Used

- Python
- Built-in Python libraries:
  - "random"
  - "string"

📂 How the Program Works

1. The program asks the user to enter the desired password length.
2. The user selects which character types to include:
   - Lowercase letters
   - Uppercase letters
   - Numbers
   - Symbols
3. The program combines the selected character sets.
4. A random password is generated using Python's "random.choice()" function.
5. The generated password and its length are displayed.
6. The user can generate another password if needed.

▶️ How to Run the Program

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in a terminal or IDE.
4. Run the program using:

python password_generator.py

💻 Example Output

========== RANDOM PASSWORD GENERATOR ==========

Enter password length: 10

Select character types:
Include lowercase letters? (yes/no): yes

Include uppercase letters? (yes/no): yes

Include numbers? (yes/no): yes

Include symbols? (yes/no): no

Lowercase letters added
Uppercase letters added
Numbers added

Generated Password: A8dkL2pQz1

Password Length: 10

Password generated successfully!

📚 Learning Purpose

This project helps beginners understand:

- Python functions
- Loops
- User input
- String handling
- Random module usage
