from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key created and saved to 'secret.key'")

def get_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: 'secret.key' file not found. Please run create_key() first.")
        return None

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

if __name__ == "__main__":
    # create_key() # Only once - First time

    key = get_key()
    if key:
        secret = "SecretPassword321"

        encrypted = encrypt_message(secret, key)
        print("Encrypted value:", encrypted)

        decrypted = decrypt_message(encrypted, key)
        print("Decrypted value:", decrypted)

