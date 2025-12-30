import base64
from cryptography.fernet import Fernet
from django.conf import settings

key = base64.urlsafe_b64encode(settings.SECRET_KEY[:32].encode())
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()
