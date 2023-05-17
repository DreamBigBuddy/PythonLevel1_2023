# More While Loops

import random

answer = random.randint(1, 100)

guess = int(input("Enter a guess: "))

while guess != answer:
    print("Incorrect!")
    guess = int(input("Enter a guess: "))

print("Correct!")
