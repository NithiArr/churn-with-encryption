from django.shortcuts import render
from base.models import customer
import pickle
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from django.contrib import messages


# Function to generate a secure key using PBKDF2
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # You can adjust the number of iterations based on your security requirements
        backend=default_backend()
    )
    return kdf.derive(password)

# Encrypt using AES algorithm in CFB mode
def encrypt(a, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)

    encryptor = cipher.encryptor()
            # Convert the value to bytes
    value_bytes = str(a).encode('utf-8')
            # Encrypt the data
    encrypted_value = encryptor.update(value_bytes) + encryptor.finalize()
    b = base64.b64encode(encrypted_value).decode()
    dec =base64.b64encode(b.encode()).decode()
    decoded_bytes = base64.b64decode(dec.encode())
    return int.from_bytes(decoded_bytes, byteorder='big')




# Example password and salt (for demonstration purposes only)
password = b'SecurePassword123'
salt =b'D\x80\xe3\x94N\n\xffA\x05K\xee\xb0\xf7M\xdd\xdf'

print(salt)
# Generate a secure key
key = generate_key(password, salt)
iv =b'\x01\xebR@G\xd6\xdd@\xff\xcc\xb3:\xd6\xad\xae\xbf'
print(iv) 

def home(request):
    return render(request,'home.html')

def store(request):
    if request.method == 'POST':
        cus = customer()
        cus.CustomerId	= encrypt(str(request.POST.get('cid')),key,iv)
        cus.Surname	= encrypt(str(request.POST.get('name')),key,iv)
        cus.CreditScore	= encrypt(int(request.POST.get('cs')),key,iv)
        cus.Geography	= encrypt(str(request.POST.get('geo')),key,iv)
        cus.Gender	    = encrypt(str(request.POST.get('gender')),key,iv)
        cus.Age	        = encrypt(int(request.POST.get('age')),key,iv)
        cus.Tenure	    = encrypt(int(request.POST.get('tenure')),key,iv)
        cus.Balance	    =encrypt(int(request.POST.get('balance')),key,iv)
        cus.NumOfProducts= encrypt(int(request.POST.get('product'))	,key,iv)
        cus.HasCrCard= encrypt(int(request.POST.get('cc')),key,iv)
        cus.IsActiveMember	=encrypt(int(request.POST.get('active')),key,iv)
        cus.EstimatedSalary = encrypt(int(request.POST.get('salary')),key,iv)
        cus.save()
        messages.success(request,"THE CUSTOMER DETAILS SUCCESSFULLY...!")
        return render(request,'home.html')
        
        