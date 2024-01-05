#Random Password Generator using Python

import random

lower_letters="abcdefghijklmnopqrst"
upper_letters="ABCDEFGHIJKLMNOPQRST"
symbols="(){},:;,_-?/|"
digit="0123456"
upper,lower,sym,dig = True,True,True,True
password=""
if upper:
    password=password + upper_letters 
if lower:
    password=password + lower_letters 
if sym:
    password= password + symbols
if dig :
    password=password + digit

strength = 13
amount = 11
print("\n Our Required Possible Generated passwords From Gievn Inputs Are : \t")

for x in range(amount):
  
   Password="".join(random.sample(password,strength))
   print("\n")
   print(Password)
