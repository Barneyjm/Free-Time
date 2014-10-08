#types of elevators, cables, buildings
from objects import *


class Models(object):
    def __init__(self):
        pass
    
    ######### elevators ##########
    # self, cur_floor, cur_weight, cur_speed, cur_accl,
    #         weight_limit, speed_limit, cable_type)


    E_basic = Elevator(0, 500, 0, 0, 3000, 20, "dunno")
    E_medium = Elevator(0, 750, 0, 0, 5000, 30, "dunno")
    E_advanced = Elevator(0, 1000, 0, 0, 10000, 40, "dunno")


    ######### cables #############
    #(self, safety_rating, max_tension, mass_per_len)
    """
    C_basic = Cable(3, 30000, 100)
    C_medium = Cable(4, 50000, 125)
    C_advanced = Cable(5, 100000, 150)
    """
    ######### buildings ##########
    #(self, num_floors, floor_cap, num_elevators)

    B_basic = Building(10, 100, 1)
    B_medium = Building(20, 300, 3)
    B_advanced = Building(30, 500, 6)

    

    ######### persons ##########
    #(self, ID, happiness, mass, cur_floor, dest_floor

    P_small = Person(0, 7, 0)
    P_medium = Person(0, 3, 0)
    P_large = Person(0, 4, 0)


if __name__ == "__main__":
    basic = Models.E_basic

    print basic.cur_weight

    p_basic = Models.P_small

    print p_basic.happiness

    b_basic = Models.B_basic
    print b_basic.waiting.keys()
