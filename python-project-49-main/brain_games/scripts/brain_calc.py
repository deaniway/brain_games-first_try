import random


def random_mat():

    global result

    num1 = random.randrange(10)
    num2 = random.randrange(10)
    chi = random.choice(['+', '-', '*'])

    if chi == '+':
        result = num1 + num2
    if chi == '-':
        result = num1-num2
    if chi == '*':
        result = num1 * num2

    print(f'Question {num1} {chi} {num2}')

    user = int(input('Your answer: '))
    if user == result:
        print("Correct!")
        return True

    else:
        print(f"{user} is wrong answer ;(. Correct answer was {result} ")
        return False
