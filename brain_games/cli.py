from prompt import string as ps

def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = ps('May I have your name?')
    print(f'Hello, {user_name}')
    return user_name

