count = 0
while count < 10:
    team_of_the_year = input("Enter the item you got: ")
    if team_of_the_year != "":
        count += 1
        print(count)
    else:
        print("You are guaranteed to get a Team Of The Year in your next pack!")
