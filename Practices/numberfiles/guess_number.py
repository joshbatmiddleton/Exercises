import random
number = random.randint(0, 100)
count = 0

guess = int(input("Guess the number: "))
while guess != number and count < 10:
    count += 1
    if guess < number:
        guess = int(input("That's too low, try again: "))
    else:
        guess = int(input("That's too high, try again: "))
if guess == number:
    print(f"You got it in {count} guesses!")
else:
    print("You have used up all of your guesses")
