from django.shortcuts import render
from base.models import customer
from django.db.models import Q
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import pandas as pd
import pickle
# Create your views here.
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
    dec = base64.b64encode(encrypted_value).decode()
    b = base64.b64encode(dec.encode()).decode()
    decoded_bytes = base64.b64decode(b.encode())
    return int.from_bytes(decoded_bytes, byteorder='big')




# Example password and salt (for demonstration purposes only)
password = b'SecurePassword123'
salt =b'D\x80\xe3\x94N\n\xffA\x05K\xee\xb0\xf7M\xdd\xdf'

print(salt)
# Generate a secure key
key = generate_key(password, salt)
iv =b'\x01\xebR@G\xd6\xdd@\xff\xcc\xb3:\xd6\xad\xae\xbf'
print(iv) 


def predict(request):
    if request.method == 'POST':
        id = encrypt((request.POST.get('sno')),key,iv)
        print(id)
        cus = customer.objects.all()
        if id:
            cus = cus.filter(Q(CustomerId__icontains=id)).first()
            CreditScore	= cus.CreditScore
            Geography	= cus.Geography     
            Gender	    = cus.Gender       
            Age	        = cus.Age
            Tenure	    = cus.Tenure 
            Balance	    = cus.Balance
            NumOfProducts= 	cus.NumOfProducts
            HasCrCard= cus.HasCrCard
            IsActiveMember	= cus.IsActiveMember       
            EstimatedSalary = cus.EstimatedSalary 
            x = pd.DataFrame({
            'CreditScore': [CreditScore],
            'Geography':[Geography],
            'Gender':[Gender],
            'Age':[Age] ,
            'Tenure':[Tenure] ,
            'Balance': [Balance],
            'NumOfProducts':[NumOfProducts] ,
            'HasCrCard': [HasCrCard],
            'IsActiveMember':[IsActiveMember],
            'EstimatedSalary':[EstimatedSalary]
             })
            cat_boost = pickle.load(open('cat_boost.sav','rb'))
            res = cat_boost.predict(x)
            return render(request,'predict.html',{'details':res})
        else:
            str='Pls enter valid ID'
            return render(request,'predict.html',{'cont':str})
             
        
    else:
        return render(request,'predict.html')
