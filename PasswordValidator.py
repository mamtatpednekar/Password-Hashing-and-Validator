# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:16:11 2022

@author: Mamta Pednekar
"""

import bcrypt
# b converts the password into bytes
password = b"Mamta@123"
#generating hash
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

user_entered = input('Enter password to login')
user_entered = bytes(user_entered, encoding='utf-8')
if bcrypt.checkpw(user_entered, hashed):
    print("Login Successful")
else:
    print("Incorrect Credentials")


