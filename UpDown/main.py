from models import Models as models
from objects import *
import elevatorTitle
import time


class UpDown(object):
    def __init__(self, player_name, difficulty):
        self.player_name = player_name
        self.difficulty = difficulty
        self.score = 0
        self.game_stats = {"people": [] }

        if difficulty == 1:
            self.GENERATE = 4
        elif difficulty == 2:
            self.GENERATE = 6
        else:
            self.GENERATE = 10

    def start(self):

        player = self.player_name
        difficulty = self.difficulty

        print "welcome " + player
        print "you're playing on difficulty: " + str(difficulty)

        building, elevator = self.generate_initial_objects()

        self.main_loop(player, difficulty, building, elevator)


    def main_loop(self, player, difficulty, building, elevator):
        cmd = ""
        
        self.generate_people(building, random.randint(2, self.GENERATE))

        
        while cmd != "4":
            
            cur_floor = elevator.cur_floor
            #self.collect_passengers(building, elevator)
            try:
                for passenger in building.waiting[cur_floor].keys():
                    cur_pass = building.waiting[cur_floor][passenger]
                    
                    if elevator.get_mass() + cur_pass.get_mass() > elevator.MASS_LIMIT:
                        print "Too much weight, trying next passenger. \nPlease remove some passengers."
                        continue
                    else:
                        elevator.add_passenger(cur_pass)                    
                        building.rm_waiting(cur_floor, cur_pass)
                        
                    cur_pass.happiness = self.calc_happiness(cur_pass)
            except:
                pass
            
            
            #self.alight_passengers(building, elevator)
            try:
                for passenger in elevator.passengers.keys():
                    cur_pass = elevator.passengers[passenger]
                    if cur_floor == cur_pass.dest_floor:
                        print "alighting passenger " + cur_pass.ID
                        cur_pass.happiness = self.calc_happiness(cur_pass)
                        self.score += cur_pass.happiness
                        self.game_stats["people"].append(cur_pass)
                        elevator.rm_passenger(cur_pass)
                    else:
                        pass
            except KeyError:
                print "error"

            print "your score: " + str(self.score)
            print "The elevator is on floor " + str(elevator.cur_floor) + ".\n"
            print """options:  \n\t move elevator (1) \n\t who's riding? (2)\n\t who's waiting? (3) \n\t quit(4)"""
            cmd = raw_input("What would you like to do? ").lower()
            
            if cmd == "quit" or cmd == "4":
                stats = self.calc_stats(building, elevator)
                print stats                
                break
            
            elif cmd == "1":
                floor = int(raw_input("Which floor? "))
                self.move_elevator(elevator, floor)
                self.generate_people(building, random.randint(2, self.GENERATE))


            elif cmd == "2":
                self.whos_riding(elevator)

            elif cmd == "3":
                self.whos_waiting(building)
                
            else: continue

            

    def calc_stats(self, building, elevator):
        score = self.score
        people = self.game_stats["people"]
        num_delivered = len(people)
        max_life = [0, "", ""]
        min_life = [300, "", ""]

        
        for person in people:
            life = person.death - person.born
            if life > max_life[0]:
                max_life[0] = life
                max_life[1] = person
                
            if life < min_life[0]:
                min_life[0] = life
                min_life[1] = person
                

        still_waiting = []
        for floor in building.waiting.keys():
            for person in building.waiting[floor].keys():
                still_waiting.append( building.waiting[floor][person])

        return num_delivered, max_life, min_life, len(still_waiting)
                
            
            

    def calc_happiness(self, cur_pass):
        return cur_pass.happiness - int(time.clock())
            

    def collect_passengers(self, building, elevator):
        print "collect passengers"
        try:
            for passenger in building.waiting[cur_floor].keys():
                cur_pass = building.waiting[cur_floor][passenger]
                elevator.add_passenger(cur_pass)
                building.rm_waiting(cur_floor, cur_pass)
        except:
            pass

    def alight_passengers(self, building, elevator):
        print "alight passengers"
        try:
            for passenger in elevator.passengers.keys():
                cur_pass = elevator.passengers[passenger]
                if cur_floor == cur_pass.dest_floor:
                    self.score += cur_pass.happiness
                    elevator.rm_passenger(cur_pass)
                else:
                    pass
        except:
            pass

    def generate_initial_objects(self):
        building = models.B_basic
        elevator = models.E_basic

        return building, elevator

    def generate_people(self, building, to_generate):
        for person in range(to_generate):
            cur_floor = random.randint(0,building.num_floors-1)
            dest_floor = random.randint(0,building.num_floors-1)
            
            person = Person(cur_floor, dest_floor, int(time.clock()))
            building.waiting[cur_floor][person.ID] = person
            

        
        
    def move_elevator(self, elevator, dest_floor):
        elevator.cur_floor = dest_floor

    def whos_waiting(self, building):
        print
        print "Floor, Num_Waiting"
        for floor in building.waiting.keys():
            print floor, len(building.waiting[floor].keys())

    def whos_riding(self, elevator):
        print
        print "Who's riding?"
        for passenger in elevator.passengers.keys():
            print elevator.passengers[passenger]








if __name__ == "__main__":

    name = raw_input("What's your name? ")
    difficulty = raw_input("Difficulty? (1 (easy), 2 (medium), 3 (hard)) ")
    
    game = UpDown("James", 1)
    game.start()
