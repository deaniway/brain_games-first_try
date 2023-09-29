#!/usr/bin/env python3
from math import gcd
import random


def game_gcd():

    num1 = random.randrange(10)
    num2 = random.randrange(10)
    print(f'Question: {num1} {num2}')

    result = gcd(num1, num2)

    user = int(input('Your answer: '))

    if user == result:
        print("Correct!")
        return True

    else:

        print(f"{user} is wrong answer ;(. Correct answer was {result}")
        return False
