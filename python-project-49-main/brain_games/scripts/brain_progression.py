import random


def game_progression():

    num1 = random.randrange(5, 10)
    num2 = random.randrange(40, 50)
    num3 = random.randrange(3, 6)

    lst = []
    for i in range(num1, num2, num3):
        lst.append(i)

    sicret_num = '..'
    random_num = random.choice(lst)
    index = lst.index(random_num)
    lst[index] = sicret_num
    print(lst)

    input_user = int(input('Your answer: '))

    if input_user == random_num:
        print("Correct!")
        return True
    else:
        print(f"{input_user} is wrong answer ;(."
              f" Correct answer was {random_num}")
        return False
