from django.test import TestCase
from .encryption import encrypt_data, decrypt_data

class EncryptionTest(TestCase):
    def test_encryption_cycle(self):
        data = "123456789012"
        encrypted = encrypt_data(data)
        decrypted = decrypt_data(encrypted)
        self.assertEqual(data, decrypted)
