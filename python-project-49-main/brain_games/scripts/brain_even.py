#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user


def main():

    name = welcome_user()

    con = 0
    while con < 3:
        num = random.randrange(1, 100)
        print(f'Question: {num}')
        result = input('Your answer: ')
        if (num % 2 == 0 and result == 'yes') or \
                (num % 2 != 0 and result == 'no'):
            con += 1
            print('Correct!')

        else:
            if num % 2 == 0 and result == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")

            elif num % 2 != 0 and result == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
            break

    if con == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
