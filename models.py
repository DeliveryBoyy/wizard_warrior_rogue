from random import randint

from exceptions import EnemyDown, GameOver
from settings import PLAYER_LIVES


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    """
    Since player/computer choice is an int between 1 and 3, we can simply subtract the defense int from the attack int
    to get the fight result. There can only be 9 different outcomes: draw result always equals 0, win result is either
    -1 or -2 and the lose result is either -2 or 1.
    """
    @staticmethod
    def fight(attack, defense):
        if (attack - defense) in [-1, 2]:
            # Win - result is either -1 or 2
            return 1
        elif attack - defense:
            # Lose - result is not zero.
            return -1
        else:
            # Draw
            return 0

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise GameOver

    def attack(self, enemy_object):
        attack_result = self.fight(int(input('Choose your attacker:\n1. Wizard\n2. Warrior\n3. Rogue\n')),
                                   enemy_object.select_attack())
        if attack_result == 1:
            return 'You attacked successfully!'
        elif attack_result:
            return 'You missed!'
        else:
            return 'It\'s a draw!'

    def defense(self, enemy_object):
        defense_result = self.fight(enemy_object.select_attack(),
                                    int(input('Choose your attacker:\n1. Wizard\n2. Warrior\n3. Rogue\n')))
        if defense_result == -1:
            return 'You defended successfully!'
        elif defense_result:
            self.decrease_lives()
            return 'You were hit!'
        else:
            return 'It\'s a draw!'


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise EnemyDown
