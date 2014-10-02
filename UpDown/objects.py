

class Elevator(object):
    def __init__(self, cur_floor, cur_weight, cur_speed, cur_accl,
                 weight_limit, speed_limit, cable_type):
        self.cur_floor = cur_floor
        self.cur_weight = cur_weight   #kg
        self.cur_speed = cur_speed     #m/s
        self.cur_accl = cur_accl       #m/s^2

        self.SPEED_LIMIT = speed_limit    #m/s
        self.WEIGHT_LIMIT = weight_limit  #kg
        
        self.cable = Cable(cable_type)
        self.num_passenger = 0


    ############# physics methods ############

    def get_weight(self):
        return self.cur_weight

    def set_weight(self, weight):
        self.cur_weight = weight

    def is_overweight(self):
        return self.cur_weight > self.WEIGHT_LIMIT

    def get_speed(self):
        return self.cur_speed

    def set_speed(self, speed):
        self.cur_speed = speed

    def is_speeding(self, speed):
        return self.cur_speed > self.SPEED_LIMIT

    ############# passenger methods ##########

    def get_num_passenger(self):
        return self.num_passenger

    def set_num_passenger(self, passengers):
        self.num_passenger = passengers

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
    def __init__(self, num_floors, floor_cap, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators

        self.floors = range(self.num_floors)
        
        self.floor_capacity = floor_capacity

        self.MAX_CAPACITY = self.num_floors*self.floor_capacity


class Person(object):
    def __init__(self, height, mass):
        self.height = height    #m
        self.mass = mass        #kg
        self.vol = self.height / self.mass #not really volume...


    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass

    def get_vol(self):
        return self.vol

    def recalc_vol(self, vol):
        self.vol = self.height / self.mass

        


    

    
