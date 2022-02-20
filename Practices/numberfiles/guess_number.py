import random
number = random.randint(0, 10)

guess = int(input("Guess the number: "))
while guess != number:
    guess = int(input("Wrong. Try again: "))
print("You got it!")
