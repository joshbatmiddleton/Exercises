number_to_be_averaged = int(input("How many numbers do you want to average? "))
counter = 1
total = 0
while counter != number_to_be_averaged + 1:
    number = int(input(f"Enter number {counter} "))
    total += number
    counter += 1
print(f"Total is {total}")
