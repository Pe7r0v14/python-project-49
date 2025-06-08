from prompt import string as ps
from random import randint as rr

def main():
    user_name = ps('Welcome to the Brain Games!\nMay I have your name?\n>>')
    print(f'Hello, {user_name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start = 0
    while start < 3:
        question=rr(1,50)
        answer=ps(f'Question: {question}\nYour answer:')
        if question % 2 == 0 and answer=='yes':
            print('Correct')
            start += 1
        elif question % 2 != 0 and answer=='no':
            print('Correct')
            start += 1
        else:
            print(f"Let's try again, {user_name}!")
            break
    print('Congratulation!')


if __name__ == '__main__':
    main()
