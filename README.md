import random
import string
import secrets
import argparse

def generate_password(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
    exclude_chars=""
):
    """
    Generate a cryptographically secure random password.
    
    Args:
        length (int): Length of the password (default: 16)
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_symbols (bool): Include special symbols
        exclude_chars (str): Characters to exclude from the password
    
    Returns:
        str: Generated password
    """
    charset = ""

    if use_uppercase:
        charset += string.ascii_uppercase
    if use_lowercase:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    # Remove excluded characters
    for ch in exclude_chars:
        charset = charset.replace(ch, "")

    if not charset:
        raise ValueError("At least one character type must be selected.")

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Ensure at least one character from each selected category
    guaranteed = []
    if use_uppercase:
        pool = "".join(c for c in string.ascii_uppercase if c not in exclude_chars)
        if pool:
            guaranteed.append(secrets.choice(pool))
    if use_lowercase:
        pool = "".join(c for c in string.ascii_lowercase if c not in exclude_chars)
        if pool:
            guaranteed.append(secrets.choice(pool))
    if use_digits:
        pool = "".join(c for c in string.digits if c not in exclude_chars)
        if pool:
            guaranteed.append(secrets.choice(pool))
    if use_symbols:
        pool = "".join(c for c in string.punctuation if c not in exclude_chars)
        if pool:
            guaranteed.append(secrets.choice(pool))

    # Fill the rest of the password
    remaining_length = length - len(guaranteed)
    rest = [secrets.choice(charset) for _ in range(remaining_length)]

    # Shuffle to avoid predictable positions
    password_list = guaranteed + rest
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


def get_strength(password):
    """Evaluate password strength."""
    score = 0
    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 20: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2: return "Weak   ⚠️"
    if score <= 4: return "Fair   🔶"
    if score <= 5: return "Strong 💪"
    return "Fortress 🔒"


def generate_multiple(count=5, **kwargs):
    """Generate multiple passwords at once."""
    return [generate_password(**kwargs) for _ in range(count)]


def interactive_mode():
    """Run an interactive CLI password generator."""
    print("\n" + "=" * 45)
    print("       🔐 RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    # Get length
    while True:
        try:
            length = int(input("\nPassword length (default 16): ").strip() or 16)
            if length < 4:
                print("  ❌ Length must be at least 4.")
            else:
                break
        except ValueError:
            print("  ❌ Please enter a valid number.")

    # Get options
    def ask(prompt, default=True):
        ans = input(prompt).strip().lower()
        if ans == "": return default
        return ans in ("y", "yes", "1", "true")

    use_upper   = ask("Include uppercase letters? (Y/n): ")
    use_lower   = ask("Include lowercase letters? (Y/n): ")
    use_digits  = ask("Include digits? (Y/n): ")
    use_symbols = ask("Include symbols? (y/N): ", default=False)
    exclude     = input("Characters to exclude (leave blank for none): ").strip()

