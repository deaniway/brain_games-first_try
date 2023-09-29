from brain_games.cli import welcome_user
from brain_games.scripts.brain_gcd import game_gcd


def main():

    pass


hello = welcome_user()
print('Find the greatest common divisor of given numbers.')


con = 0
while con < 3:
    game = game_gcd()
    if game is True:
        con += 1
    else:
        print(f"Let's try again, {hello}!")
        break

if con == 3:
    print(f"Congratulations, {hello}!")


if __name__ == "__main__":
    main()
