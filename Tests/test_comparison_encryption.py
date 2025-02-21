import pytest
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

@pytest.fixture
def data():
    # Mock data instead of reading from CSV
    df = pd.DataFrame({
        'balance': [1000, 2000, 3000],  # Just a few sample balances
        'name': ['Alice', 'Bob', 'Charlie'],
        'account_id': ['A123', 'B456', 'C789']
    })
    return df['balance'].iloc[0]  # Return just the first balance value (adjust as necessary)

@pytest.fixture
def key():
    # Mock key for AES encryption
    return b'16-byte-key-for-encryption'  # This is a 16-byte key for AES-128

def test_aes_encryption(data, key):
    # Mock AES encryption function
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'16-byte-iv-vector'), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding to match AES block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(str(data).encode()) + padder.finalize()

    # Encrypt data
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    assert len(encrypted) > 0  # Check that something was encrypted

def test_key(data, key):
    # Simple test to ensure key is correctly mocked
    assert isinstance(key, bytes)
    assert len(key) == 16  # AES-128 requires a 16-byte key

