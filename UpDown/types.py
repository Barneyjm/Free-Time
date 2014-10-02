#types of elevators, cables, buildings
import objects

######### elevators ##########
# self, cur_floor, cur_weight, cur_speed, cur_accl,
#         weight_limit, speed_limit, cable_type)


E_basic = Elevator(0, 500, 0, 0, 3000, 20, "dunno")
E_medium = Elevator(0, 750, 0, 0, 5000, 30, "dunno")
E_advanced = Elevator(0, 1000, 0, 0, 10000, 40, "dunno")


######### cables #############
#(self, safety_rating, max_tension, mass_per_len)

C_basic = Cable(3, 30000, 100)
C_medium = Cable(4, 50000, 125)
C_advanced = Cable(5, 100000, 150)

######### buildings ##########
#(self, num_floors, floor_cap, num_elevators)

B_basic = Building()
B_medium = Building()
B_advanced = Building()



######### persons ##########
#(self, height, mass)

P_small = Person()
P_medium = Person()
P_large = Person()
