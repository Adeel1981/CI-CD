import time
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from phe import paillier

# Function to encrypt data using AES
def aes_encrypt(data, key):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00'*16), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

# Function to decrypt data using AES
def aes_decrypt(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00'*16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    return data.decode()

# AES encryption test (simplified)
def test_aes_encryption(data, key):
    start_time = time.time()
    encrypted_data = aes_encrypt(data, key)
    encryption_time = time.time() - start_time
    decrypted_data = aes_decrypt(encrypted_data, key)
    decryption_time = time.time() - start_time

    return encrypted_data, decrypted_data, encryption_time, decryption_time

# Paillier encryption function
def paillier_encrypt(data, public_key):
    return public_key.encrypt(data)

# Paillier decryption function
def paillier_decrypt(encrypted_data, private_key):
    return private_key.decrypt(encrypted_data)

# Paillier encryption test
def test_paillier_encryption(data, public_key, private_key):
    start_time = time.time()
    encrypted_data = paillier_encrypt(data, public_key)
    encryption_time = time.time() - start_time
    decrypted_data = paillier_decrypt(encrypted_data, private_key)
    decryption_time = time.time() - start_time

    return encrypted_data, decrypted_data, encryption_time, decryption_time


# Unit tests for AES and Paillier comparison
class TestEncryptionComparison(unittest.TestCase):

    def test_encryption_comparison(self):
        # Load the dataset
        df = pd.read_csv("data/bank.csv")
        balance_value = df['balance'].iloc[0]

        # Set up AES key and Paillier keys
        key = b'\x00'*32  # AES 256-bit key
        public_key, private_key = paillier.generate_paillier_keypair()

        # Test AES encryption and decryption
        aes_encrypted, aes_decrypted, aes_encryption_time, aes_decryption_time = test_aes_encryption(str(balance_value), key)

        # Test Paillier encryption and decryption
        paillier_encrypted, paillier_decrypted, paillier_encryption_time, paillier_decryption_time = test_paillier_encryption(balance_value, public_key, private_key)

        print(f"AES Encryption Time: {aes_encryption_time:.6f} seconds")
        print(f"AES Decryption Time: {aes_decryption_time:.6f} seconds")
        print(f"Paillier Encryption Time: {paillier_encryption_time:.6f} seconds")
        print(f"Paillier Decryption Time: {paillier_decryption_time:.6f} seconds")

        self.assertEqual(balance_value, aes_decrypted, "AES Decryption failed!")
        self.assertEqual(balance_value, paillier_decrypted, "Paillier Decryption failed!")
 
