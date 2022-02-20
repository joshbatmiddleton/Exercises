count = 1
password = "MinecraftJava@1"
attempt = input("What is your password? ")
while count < 3 and attempt != password:
    attempt = input("Wrong password. Try again: ")
    count += 1
if attempt == password:
    print("Access Granted")
else:
    print("Too many attempts. Try again later.")
