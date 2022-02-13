# Integer checking function - loops until a valid number is entered



def integer_checker(question):

    error = "\nSorry, you must enter an integer\n"

    number = ""

    while not number:

        try:

            number = int(input(question))

            return number

        except ValueError:

            print(error)

# Main routine

age = integer_checker("Please enter your age: ")

print(f"Age = {age}")
