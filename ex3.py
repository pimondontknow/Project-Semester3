import random

random_number = random.randint(1, 20)
found = 0

while found == 0:
    x = input("Please enter a number: ")
    if int(x) == random_number:
        found = 1
    else:
        found = 0

print("Congratulations!")

