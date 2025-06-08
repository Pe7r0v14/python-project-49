import prompt
from random import randint

def game_answer(true_answer,user_answer,random_value = None):
    pass

#Uniq
#generation question
random_value = randint(1,25)
#generation answer
def true_answer(random_value):
    if random_value % 2 == 0:
        true_answer_callback = 'yes'
    else:
        true_answer_callback = 'no'
    return true_answer_callback
#user answer
def game():
    pass
    start = 0

def check_quest(user_answer,quest_answer):
    start = 0
    while start <= 2:
        if user_answer == quest_answer:
            print('Correct!')
            start += 1
        else:
            print('Sorry')
            break
        print('Congratulation!')
    
def game_answer():
    random_value=randint(1,25)
    if random_value % 2 == 0:
        quest_answer = 'yes'
    else:
        quest_answer = 'no'
    user_answer = prompt.string(f'"yes" if even, "no" if no\n>>>{random_value}\n>')
    start = 0
    check_quest(user_answer,quest_answer)
 

game_answer()

"""Сейчас проблема что во всех играх повторяется одна и таже логика:

    Приветствие
    Цикл от старта до финиша
    Вывод вопроса
    Получение ответа пользователя
    Поздравление с победой"""
