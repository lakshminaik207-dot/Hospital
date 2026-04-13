# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:21:39 2025

@author: admin
"""

import random
import getpass
import time
stored_username="anki"
stored_password="7777"
stored_gmailid="ankinaik@gmail.com"
def generate_otp():
    return str(random.randint(100000,999999))
def authenticate():
    print("==multi-factor authentication demo==")
    username=input("enter username:")
    password=getpass.getpass("enter password:")
    gmailid=input("enter your gmailid:")
    if username == stored_username and password == stored_password and gmailid == stored_gmailid:
       print("/n username and password correct:")
       otp=generate_otp()
       otp_time=time.time()
       print(f"(simulated)otp sent to your device:{otp}")
       user_otp=input("enter the otp:")
       if time.time()-otp_time>20:
           print("otp has expired")
       if user_otp==otp:
           print("/n login successful.multifactor authentication passed")
       else:
           print("/n invalid otp.access denide")
    else:
        print("/n invalid username or password or gmailid")
authenticate()
   