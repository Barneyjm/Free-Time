from models import Models as models
from objects import *
import elevatorTitle

import math


class UpDown(object):
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.score = 0

    def start(self, player, difficulty, score):

        print "welcome " + player
        print "you're playing on difficulty: " + str(difficulty)
        print "you have a score of: " + str(score)

        #elevator = models.E_basic
        #print elevator.cur_weight

        self.generate_initial_objects()

        self.main_loop(player, difficulty, score)


    def main_loop(player, difficulty, score):
        pass

    def generate_initial_objects(self):
        building = models.B_basic
        elevator = models.E_basic
        all_people = []
        









if __name__ == "__main__":
    game = UpDown("James", 1)
    game.start("James", 1, 0)
