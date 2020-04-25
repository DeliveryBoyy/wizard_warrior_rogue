from models import Player, Enemy
from exceptions import EnemyDown, GameOver


def play():
    # Create the player object with the name from input.
    player = Player(input('Let\'s play!\nPlease enter your name: '))
    # Create the first enemy object, level 1.
    enemy = Enemy(1)
    # Prompt for 'start' to start the game
    if input('Type \'start\' to start the game ').lower() == 'start':
        pass
    else:
        raise KeyboardInterrupt

    # Main game cycle.
    while True:
        try:
            print(player.attack(enemy))
            print(player.defense(enemy))
        except EnemyDown:
            enemy = Enemy(enemy.level + 1)
            player.score += 5


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print(f'Game over! Your Score: {player.score}')
