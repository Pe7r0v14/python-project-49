from prompt import string


def welcome_user():
    user_name = string('Whay is your name?\n>>')
    print(f'Hello, {user_name}!')
