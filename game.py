import re

from models import Player, Enemy
from exceptions import EnemyDown, GameOver
from settings import COMMANDS


def play():
    # Create the player object with the name from input.
    # The input is validated via a regex - the name can consist of 3-20 lower or uppercase latin letters and digits.
    player_name = input('Let\'s play!\nPlease enter your name:\n > ')
    player_name_entered = False
    while not player_name_entered:
        if re.search('^([a-zA-Z0-9]{3,20})$', player_name):
            player_name_entered = True
        else:
            print('The name can be 3-20 characters long. '
                  'Can consist of lowercase and uppercase latin letters and digits.\n')
            player_name = input('Please enter your name:\n > ')
    player = Player(player_name)

    # Create the first enemy object, level 1.
    enemy = Enemy(1)

    # Game menu
    start = False
    while not start:
        player_command = input('Type \'START\' to start the game, or \'HELP\' for a list of commands.\n > ').lower()
        if player_command == 'start':
            start = True
        elif player_command == 'show scores':
            with open('scores.txt', 'r') as f:
                print('{}{}{}'.format('----------\n', f.read().rstrip('\n'), '\n----------'))
        elif player_command == 'help':
            for command in COMMANDS:
                print(f'-- {command}')
        elif player_command == 'exit':
            raise KeyboardInterrupt
        else:
            raise KeyboardInterrupt

    # Main game cycle.
    while True:
        try:
            print(player.attack(enemy))
            print(player.defense(enemy))
        except EnemyDown:
            print('!!! ENEMY DOWN !!!')
            enemy = Enemy(enemy.level + 1)
            player.score += 5


if __name__ == '__main__':
    try:
        play()
    except GameOver as err:
        err.add_new_score()
        print(f'Game over! Your final score: {err.player.score}')
    finally:
        print('Goodbye!')
