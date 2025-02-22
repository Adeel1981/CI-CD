import pytest
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

@pytest.fixture
def data():
    # Mock data instead of reading from CSV
    df = pd.DataFrame({
        'balance': [1000, 2000, 3000],  # Sample balances
        'name': ['Alice', 'Bob', 'Charlie'],
        'account_id': ['A123', 'B456', 'C789']
    })
    return df['balance'].iloc[0]  # Returning first balance value

@pytest.fixture
def key():
    # Use a valid AES key (16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256)
    return b'\x00' * 32  # 32-byte key for AES-256

def test_aes_encryption(data, key):
    # Corrected AES key to be exactly 32 bytes for AES-256
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding to match AES block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(str(data).encode()) + padder.finalize()

    # Encrypt data
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    assert len(encrypted) > 0  # Ensure encryption produces output

def test_key(key):
    # Check that key has the correct size for AES-256
    assert isinstance(key, bytes)
    assert len(key) == 32  # AES-256 requires a 32-byte key
