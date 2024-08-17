from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

class RSASecurity:
    def __init__(self, private_key_pem=None, public_key_pem=None):
        self.private_key = None
        self.public_key = None
        if private_key_pem:
            self.load_private_key_from_pem(private_key_pem)
        if public_key_pem:
            self.load_public_key_from_pem(public_key_pem)

    def load_private_key_from_pem(self, pem_data):
        """Load the private key from PEM data."""
        self.private_key = serialization.load_pem_private_key(
            pem_data.encode(),
            password=None,
        )
        print("Private key loaded from PEM data")

    def load_public_key_from_pem(self, pem_data):
        """Load the public key from PEM data."""
        self.public_key = serialization.load_pem_public_key(
            pem_data.encode(),
        )
        print("Public key loaded from PEM data")

    def encrypt(self, plaintext):
        """Encrypt plaintext using the public key."""
        ciphertext = self.public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using the private key."""
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode('utf-8')
