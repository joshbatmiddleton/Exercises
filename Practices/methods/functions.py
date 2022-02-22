def say_hello(first_name, family_name):
    print(f"Hello {first_name} {family_name} from a function!")


# Main
name = input("What is your name? ")
other = input("What is your last name? ")
say_hello(name, other)
