class EnemyDown(Exception):
    pass


class GameOver(Exception):
    """
    When the exception is initiated, also initiate a Score object as one of its attributes.
    This is needed for score table manipulations after the end of the game.
    """
    def __init__(self, player):
        self.player = player
        self.scores = Score(player, 'scores.txt')

    """
    Add the new score to the table and update the score file.
    """
    def add_new_score(self):
        # Add the new score to the list of scores read from the file.
        self.scores.scores_list.append([self.player.name, self.player.score])
        # Sort the list by the second element of sub-lists (score).
        self.scores.scores_list.sort(key=lambda i: i[1], reverse=True)
        # Remove the last element being the lowest score if there is more than 10 scores saved already.
        if len(self.scores.scores_list) > 10:
            self.scores.scores_list.pop()
        # Write the scores back to the score file.
        with open('scores.txt', 'w') as f:
            index = 1
            for score in self.scores.scores_list:
                f.write(f'{index}. Player name: {score[0]} | Score: {score[1]}\n')
                index += 1


class Score:
    """
    This saves the current score from file in the scores_list attribute, which is a list that contains sub-lists of two
    elements each: the player name and their score.
    """
    def __init__(self, player, score_file):
        self.player = player
        self.scores_list = []
        with open(score_file, 'r') as f:
            for line in f.readlines():
                self.scores_list.append([line.split(' ')[3], int(line.split(' ')[-1].rstrip('\n'))])
