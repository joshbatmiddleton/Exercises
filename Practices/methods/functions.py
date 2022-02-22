def say_hello(first_name, family_name):
    return f"Hello {first_name} {family_name} from a function!"


# Main
name = input("What is your name? ")
other = input("What is your last name? ")
print(say_hello(name, other))
