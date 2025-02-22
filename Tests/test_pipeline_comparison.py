import time
import unittest
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from phe import paillier

# Function to encrypt using AES (Traditional CI)
def aes_encrypt(data, key):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00'*16), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

# Function to decrypt using AES
def aes_decrypt(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00'*16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    return data.decode()

# Function to encrypt using Paillier (CI with HE)
def paillier_encrypt(data, public_key):
    return public_key.encrypt(data)

# Function to decrypt using Paillier
def paillier_decrypt(encrypted_data, private_key):
    return private_key.decrypt(encrypted_data)

# Test class
class TestPipelineComparison(unittest.TestCase):

    def test_traditional_ci(self):
        """Test Traditional CI Encryption"""
        key = b'\x00'*32  # AES 256-bit key
        data = "12345"

        start_time = time.time()
        encrypted_data = aes_encrypt(data, key)
        decrypted_data = aes_decrypt(encrypted_data, key)
        duration = time.time() - start_time

        print(f"Traditional CI Execution Time: {duration:.6f} seconds")
        self.assertEqual(data, decrypted_data, "AES Decryption failed!")

    def test_ci_with_he(self):
        """Test CI with Homomorphic Encryption"""
        public_key, private_key = paillier.generate_paillier_keypair()
        data = 12345  # Integer for Paillier

        start_time = time.time()
        encrypted_data = paillier_encrypt(data, public_key)
        decrypted_data = paillier_decrypt(encrypted_data, private_key)
        duration = time.time() - start_time

        print(f"CI with HE Execution Time: {duration:.6f} seconds")
        self.assertEqual(data, decrypted_data, "Paillier Decryption failed!")

if __name__ == "__main__":
    unittest.main()
