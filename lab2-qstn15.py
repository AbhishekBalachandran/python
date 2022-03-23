import random
import string


password = ""
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
for i in range (8):
    password += random.choice(letters) 
for i in range (3):
    password += random.choice(numbers)
    password += random.choice(symbols)

print("The password is :" , password)