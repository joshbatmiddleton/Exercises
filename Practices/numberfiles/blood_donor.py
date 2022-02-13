age = float(input("Please enter age: "))
weight = float(input("Please enter weight: "))

if age < 16 or weight < 50:
    print("You cannot give blood! You haven't filled all of the requirements")
else:
    print("You can donate blood")
