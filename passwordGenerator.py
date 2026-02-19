import random

letters = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special = "!@#$%^&*/|"
chars = letters + number + special

print("Your Password:- ")
password = ""
for x in range(10):
    password += random.choice(chars)
    if (x+1) % 4 == 0 and x < 10:
        password+= "-"
print(password)