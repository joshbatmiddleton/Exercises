import random
number = random.randint(0, 100)
count = 1
mode = ""
while mode != "H" and mode != "M" and mode != "E":
    mode = input("Enter 'E' for Easy mode, 'M' for Medium mode or 'H' for Hard mode: ")
    if mode == "H":
        num_guesses = 3
    elif mode == "M":
        num_guesses = 5
    elif mode == "E":
        num_guesses = 10
    else:
        print("That was not an option. Try again: ")

guess = int(input("Guess the number: "))
while guess != number and count < num_guesses:
    
    count += 1
    if guess < number:
        guess = int(input("That's too low, try again: "))
    else:
        guess = int(input("That's too high, try again: "))
if guess == number:
    print(f"You got it in {count} guesses!")
else:
    print(f"You have used your guesses")
