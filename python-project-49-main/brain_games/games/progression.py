from brain_games.cli import welcome_user
from brain_games.scripts.brain_progression import game_progression


def main():

    pass


hello_name = welcome_user()
print('What number is missing in the progression?')


con = 0
while con < 3:
    game = game_progression()
    if game is True:
        con += 1
    else:
        print(f"Let's try again, {hello_name}!")
        break

if con == 3:
    print(f"Congratulations, {hello_name}!")


if __name__ == "__main__":
    main()
