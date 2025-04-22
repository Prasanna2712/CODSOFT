import random

size = int(input("Please enter the  password size (like 1,2,3,etc): "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

chars = letters + digits + special_characters

password = ""

for i in range(size):
    password += random.choice(chars)
print("Generated Password:", password)
