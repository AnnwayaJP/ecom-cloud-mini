from cryptography.fernet import Fernet

def demo():
    key = Fernet.generate_key()
    f = Fernet(key)
    secret = b"Confidential E-commerce Data"
    token = f.encrypt(secret)
    original = f.decrypt(token)
    print("Key:", key.decode())
    print("Encrypted:", token)
    print("Decrypted:", original.decode())

if __name__ == "__main__":
    demo()
