# 1- import string module
# 2- store all characters in lists (upper/lower case, digits, punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 6 or moore
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digits and punctuations

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
character_number = int(input("Enter number of characters: "))

while True:
    try:
        if character_number < 6:
            input("Enter number grater than 6: ")
            character_number = int(input("Enter number of characters: "))
        else:
            break
    except:
        print("Enter number only")
        character_number = int(input("Enter number of characters: "))

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30 / 100))
part2 = round(character_number * (20 / 100))

password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
random.shuffle(password)
password = "".join(password[0:])

print(password)