#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_calc import random_mat


hello = welcome_user()
print('What is the result of the expression?')
con = 0
while con < 3:
    game = random_mat()

    if game is True:
        con += 1
    else:
        print(f"Let's try again, {hello}!")
        break

if con == 3:
    print(f"Congratulations, {hello}!")
