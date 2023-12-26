import random

sample_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

for i in range(50):
    first = "" 
    second = ""
    third = ""

    for f in range(24):
        first += random.choice(sample_chars)
    
    for f in range(6):
        second += random.choice(f"{sample_chars}_")

    for f in range(27):
        third += random.choice(sample_chars)

    token = f"{first}.{second}.{third}"

    output = open("tokens.txt", "a")
    output.write(f"{token}\n")
