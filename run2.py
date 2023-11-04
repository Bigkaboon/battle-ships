import random

user_name = ""


def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def validate_input(current_input, valid_options):
    return current_input in valid_options

def get_user_name():
    user_name = input("Enter a username \n")
    while len(user_name) < 3:
        return user_name