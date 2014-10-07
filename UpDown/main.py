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

        building, elevator = self.generate_initial_objects()

        self.main_loop(player, difficulty, score, building, elevator)


    def main_loop(self, player, difficulty, score, building, elevator):
        cmd = ""
        self.generate_people(building, random.randint(2, 10))

        
        while cmd != "quit" or cmd == "4":

            print "The elevator is on floor " + str(elevator.cur_floor) + ".\n"
            print """options:  \n\t move elevator (1) \n\t who's riding? (2)\n\t who's waiting? (3) \n\t quit(4)"""
            cmd = raw_input("What would you like to do? ").lower()
            
            if cmd == "quit" or cmd == "4":
                break
            
            elif cmd == "move elevator" or cmd == "1":
                floor = int(raw_input("Which floor? "))
                self.move_elevator(elevator, floor)
                self.generate_people(building, random.randint(2, 10))


            elif cmd == "who's riding?" or cmd == "2":
                print self.whos_riding(elevator)
                #get more detailed info later

            elif cmd == "who's waiting?" or cmd == "3":
                print self.whos_waiting(building)
                #get more detailed info later
                
            else: continue

            cur_floor = elevator.cur_floor
            elevator.passengers = building.waiting[cur_floor]
            print elevator.passengers
            print
            try:
                for passenger in elevator.passengers.keys():
                    print passenger
                    building.rm_waiting(cur_floor, passenger)
                print elevator.passengers
            except:
                pass

    def generate_initial_objects(self):
        building = models.B_basic
        elevator = models.E_basic

        return building, elevator

    def generate_people(self, building, to_generate):
        for person in range(to_generate):
            cur_floor = random.randint(0,building.num_floors-1)
            dest_floor = cur_floor % 7
            
            person = Person(cur_floor, dest_floor)
            building.waiting[cur_floor][person.ID] = person
            

        
        
    def move_elevator(self, elevator, dest_floor):
        elevator.cur_floor = dest_floor

    def whos_waiting(self, building):
        print "who's waiting?"
        for floor in building.waiting.keys():
            print floor, len(building.waiting[floor].keys())

    def whos_riding(self, elevator):
        print "who's riding?"
        return elevator.passengers








if __name__ == "__main__":
    game = UpDown("James", 1)
    game.start("James", 1, 0)
