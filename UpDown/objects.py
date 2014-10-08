import binascii
import os
import random

class Elevator(object):
    def __init__(self, cur_floor, cur_mass, cur_speed, cur_accl,
                 mass_limit, speed_limit, cable_type):
        self.cur_floor = cur_floor
        self.cur_mass = cur_mass   #kg
        self.cur_speed = cur_speed     #m/s
        self.cur_accl = cur_accl       #m/s^2

        self.SPEED_LIMIT = speed_limit    #m/s
        self.MASS_LIMIT = mass_limit  #kg
        
        #self.cable = Cable(cable_type)

        self.passengers = dict()


    ############# physics methods ############

    def get_mass(self):
        return self.cur_mass

    def set_mass(self, mass):
        self.cur_mass = mass

    def is_overweight(self):
        return self.cur_mass > self.MASS_LIMIT

    def get_speed(self):
        return self.cur_speed

    def set_speed(self, speed):
        self.cur_speed = speed

    def is_speeding(self, speed):
        return self.cur_speed > self.SPEED_LIMIT

    ############# passenger methods ##########

    def get_num_passenger(self):
        return len(self.passengers.keys())

    def add_passenger(self, passenger):
        self.passengers[passenger.ID] = passenger

    def rm_passenger(self, passenger):
        del self.passengers[passenger.ID]

    ############# floor methods ##############

    def get_floor(self):
        return self.cur_floor

    def set_floor(self, floor):
        #ensure floor doesn't exceed building limit
        self.cur_floor = floor

    def up_floor(self):
        self.cur_floor += 1

    def dwn_floor(self):
        self.cur_floor -= 1

    def is_above(self, floor):
        return self.cur_floor < floor
    
            
class Cable(object):
    def __init__(self, safety_rating, max_tension, mass_per_len):
        self.safety_rating = safety_rating #number of "breaks" before it fails
        self.cur_tension = self.set_tension(mass, accl=10)
        
        self.MAX_TENSION = max_tension
        self.MASS_PER_LEN = mass_per_len
    

    ######## cable safety ###########
    def get_safety_rating(self):
        return self.safety_rating

    def set_safety_rating(self, safety_rating):
        self.safety_rating = safety_rating

    def dec_safety_rating(self, dec=1):
        self.safety_rating -= dec

        if self.safety_rating <= 0:
            self.cable_fails()

    def inc_safety_rating(self, inc=1):
        self.safety_rating += inc

    def cable_fails(self):
        #free fall
        return "Your cable has failed"

    ######## tension methods ########

    def get_tension(self):
        return self.cur_tension

    def set_tension(self, mass, accl):
        self.cur_tension = mass * accl

    def is_over_max_tension(self):
        return self.cur_tension > self.MAX_TENSION


class Building(object):
    def __init__(self, num_floors, floor_capacity, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators

        self.floors = range(self.num_floors)
        self.waiting = dict().fromkeys(self.floors)

        for floor in self.waiting:
            self.waiting[floor] = dict()

        #print len(self.waiting.keys())
        
        self.floor_capacity = floor_capacity

        self.MAX_CAPACITY = self.num_floors*self.floor_capacity

    def get_num_waiting(self, floor):
        return len(self.waiting[floor].keys())

    def add_waiting(self, floor, passenger):
        self.waiting[floor][passenger.ID] = passenger

    def rm_waiting(self, floor, passenger):
        del self.waiting[floor][passenger.ID]
        


class Person(object):
    def __init__(self, cur_floor, dest_floor, born):
        #remove numbers except floors and auto generate them
        self.ID = self.generate_ID()
        self.happiness = self.generate_happiness()
        self.mass = self.generate_mass()        #kg
        self.born = born
        self.death = -1
        
        self.cur_floor = cur_floor
        self.dest_floor = dest_floor
        
        self.wait_time = 0
        self.ride_time = 0

        ##implement later
        #self.height = height    #m
        #self.vol = self.height / self.mass #not really volume...

    def __repr__(self):
        return self.ID[0:4] + " is going to floor " + str(self.dest_floor) + " and has a happiness of " + str(self.happiness) + "."
    
    ############## unique numbers ######

    def generate_ID(self):
        return binascii.hexlify(os.urandom(4))

    def generate_happiness(self):
        return random.randint(25, 125)

    def generate_mass(self):
        return random.randint(50, 125)
        
    ############## happiness ##########
    def get_happiness(self):
        return self.happiness

    def set_happiness(self, happiness):
        self.happiness = happiness

    def calc_happiness(self):
        self.happiness = self.happiness - (self.wait_time + self.ride_time)
    
    ############# physics ##############
    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass


        ##implement later
"""
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_vol(self):
        return self.vol

    def recalc_vol(self, vol):
        self.vol = self.height / self.mass
"""
        


    
if __name__ == "__main__":
    elevator = Elevator(0,0,0,0,0,0,"none")
    building = Building(10,100, 1)

    print building.waiting.keys()
    print building.waiting[0]

    person = Person(0,9, 0)
    print person
    building.waiting[0] = {person.ID: person}
    print "currently waiting"
    print building.waiting[0]
    print building.waiting[0][person.ID].cur_floor
    print building.waiting[0][person.ID].dest_floor
    elevator.add_passenger(person)
    print "elevator"
    print elevator.passengers
    building.rm_waiting(0, person)
    print "building"
    print building.waiting[0]
    print "elevator"
    print elevator.passengers
    
