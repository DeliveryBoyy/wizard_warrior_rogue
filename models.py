"""
Module for Player and Enemy classes.
Handles the fight logic, lives, levels and in-game score tracking.
"""

from random import randint

from exceptions import EnemyDown, GameOver
from settings import PLAYER_LIVES


class Player:
    """
    Player class handles fight logic and game over state.
    """
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        Since player/computer choice is an int between 1 and 3, we can simply subtract the defense int from the attack int
        to get the fight result. There can only be 9 different outcomes: draw result always equals 0, win result is either
        -1 or -2 and the lose result is either -2 or 1.
        """
        if attack - defense in [-1, 2]:
            # Win - result is either -1 or 2
            return 1
        elif attack - defense:
            # Lose - result is not zero.
            return -1
        else:
            # Draw
            return 0

    def decrease_lives(self):
        """
        Decrement the player Lives and end the game if there are no lives left.
        """
        self.lives -= 1
        if not self.lives:
            raise GameOver(self)

    def attack(self, enemy_object):
        """
        Attack logic and user input.
        """
        attack_result = self.fight(int(input('Choose your attacker:\n1. Wizard\n2. Warrior\n3. Rogue\n > ')),
                                   enemy_object.select_attack())
        if attack_result == 1:
            self.score += 1
            enemy_object.decrease_lives()
            return 'You attacked successfully!'
        elif attack_result:
            return 'You missed!'
        else:
            return 'It\'s a draw!'

    def defense(self, enemy_object):
        """
        Defense logic and user input.
        """
        defense_result = self.fight(enemy_object.select_attack(),
                                    int(input('Choose your defender:\n1. Wizard\n2. Warrior\n3. Rogue\n > ')))
        if defense_result == -1:
            return 'You defended successfully!'
        elif defense_result:
            self.decrease_lives()
            return 'You were hit!'
        else:
            return 'It\'s a draw!'


class Enemy:
    """
    Enemy class, handles Enemy attack/defense choice and Enemy defeat.
    """
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
