# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.backends import default_backend

# class RSA_Security:
#     def __init__(self, key_size=2048):
#         self.key_size = key_size
#         self.private_key = None
#         self.public_key = None

#     def generate_keys(self):
#         """Generate a new RSA key pair."""
#         self.private_key = rsa.generate_private_key(
#             public_exponent=65537,
#             key_size=self.key_size,
#             backend=default_backend()
#         )
#         self.public_key = self.private_key.public_key()

#     def serialize_private_key(self):
#         """Serialize the private key to PEM format."""
#         return self.private_key.private_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PrivateFormat.PKCS8,
#             encryption_algorithm=serialization.NoEncryption()
#         )

#     def serialize_public_key(self):
#         """Serialize the public key to PEM format."""
#         return self.public_key.public_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PublicFormat.SubjectPublicKeyInfo
#         )

#     def encrypt(self, plaintext):
#         """Encrypt plaintext using the public key."""
#         ciphertext = self.public_key.encrypt(
#             plaintext.encode(),
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return ciphertext

#     def decrypt(self, ciphertext):
#         """Decrypt ciphertext using the private key."""
#         plaintext = self.private_key.decrypt(
#             ciphertext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return plaintext.decode('utf-8')

# if __name__=='__main__':

#     # Example Usage:
#     rsa_secure = RSA_Security()
#     rsa_secure.generate_keys()  # Generate RSA key pair

#     # Serialize and print keys (optional)
#     private_key_pem = rsa_secure.serialize_private_key()
#     public_key_pem = rsa_secure.serialize_public_key()
#     print(f"Public Key:\n{public_key_pem.decode()}")
#     print(f"Private Key:\n{private_key_pem.decode()}")

#     # Encrypt and decrypt a message
#     plaintext = "This is a highly secure message."
#     print(f"Plaintext: {plaintext}")

#     ciphertext = rsa_secure.encrypt(plaintext)
#     print(f"Ciphertext: {ciphertext}")

#     decrypted_text = rsa_secure.decrypt(ciphertext)
    # print(f"Decrypted Text: {decrypted_text}")
