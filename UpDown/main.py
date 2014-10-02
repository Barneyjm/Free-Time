import objects
import types
import elevatorTitle


class UpDown(object):
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty

    def start(self):
        #print elevatorTitle.title

        print "welcome " + self.player_name
        print "you're playing on difficulty: " + str(self.difficulty)

        
        










if __name__ == "__main__":
    game = UpDown("James", 1)
    game.start()
