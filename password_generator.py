import secrets  # Generate secure random choices.
import string  # Provide letters, digits, and symbols.

characters = string.ascii_letters + string.digits + "!@#$%^&*"  # Set the character pool.
password = "".join(secrets.choice(characters) for _ in range(16))  # Generate a password.
print("Generated password:", password)  # Display the result.
