age = float(input("Please enter age: "))
temp = float(input("Please enter temp: "))

if age < 2 and temp >= 38:
    print("Call a doctor!")
elif temp > 39.5:
    print("High fever")
else:
    print("You're fine")
