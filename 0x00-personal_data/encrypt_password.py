#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid


# Example usage
if __name__ == "__main__":
    # Hash a password
    password = "my_secure_password"
    hashed_password = hash_password(password)
    print(f"Hashed password: {hashed_password}")

    # Validate the password
    is_correct = is_valid(hashed_password, "my_secure_password")
    print(f"Password is valid: {is_correct}")

    # Validate with an incorrect password
    is_correct = is_valid(hashed_password, "wrong_password")
    print(f"Password is valid: {is_correct}")
