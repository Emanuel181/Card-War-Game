import string


def validation_for_name():
    allowed = [letter for letter in string.ascii_uppercase + string.ascii_lowercase + ' ']
    name = input()
    if len(name) < 3:
        return False
    for letter in name:
        if letter not in allowed:
            return False
    return name


def validate_user_choice(choice):
    return choice in ['1', '0']