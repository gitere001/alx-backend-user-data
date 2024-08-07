import base64

def decode_base64(encoded_str: str) -> bytes:
    """Decode a Base64 encoded string."""
    try:
        # Decode Base64
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes
    except (TypeError, base64.binascii.Error) as e:
        print(f"Decoding failed: {e}")
        return None

# Base64 encoded values
encoded_email = "9f65ec1d-7033-40ce-b788-dc7840848bfe"
encoded_password = "5b107592d7fec12bf49de17cf5507865644fb9272b842fb8a23a69a2b4c58a0b"

# Decode
decoded_email_bytes = decode_base64(encoded_email)
decoded_password_bytes = decode_base64(encoded_password)

print("Decoded Email Bytes:", decoded_email_bytes)
print("Decoded Password Bytes:", decoded_password_bytes)

# If the data is indeed text, you can try decoding it later
try:
    decoded_email = decoded_email_bytes.decode('utf-8')
    decoded_password = decoded_password_bytes.decode('utf-8')
    print("Decoded Email:", decoded_email)
    print("Decoded Password:", decoded_password)
except (AttributeError, UnicodeDecodeError) as e:
    print(f"Decoding to UTF-8 failed: {e}")
