# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:43:54 2014

Models the consituent parts of the Block Tower game.

@author: James
"""

import numpy as np

class Block(object):
    """
    The basic building block of the game
    Right now, presumed to be rectangular
    """
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth
        self.dimensions = np.array([self.length, self.width, self.depth])
        self.mass_center = self.dimensions/2
#        self.orientation = orientation
        self.in_place = True
        
    def set_state(self, state):
        self.in_place = state


class Layer(object):
    """
    A layer is made up of n Block objects
    """
    def __init__(self, blocks_wide, orientation):
        self.blocks_wide = blocks_wide
        self.orientation = orientation
        
        block = Block(3, 1, 1)
        self.layer = np.array([block]*self.blocks_wide)
        
    def layer_mass_center(self):
        for block in self.layer:
            if block.in_place:
                pass
            
    def remove_block(self, block_coord):
        self.layer[block_coord].set_state(False)            
        
    
class Tower(object):
    """
    A tower is made of n Layer objects
    """
    def __init__(self, height):
        self.height = height
        layer = Layer(3, 1)
        self.tower = np.array([layer]*self.height)


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def increment_score(self):
        self.score += 1
        
    def winner(self):
        print self.name + " is the winner!"
        
        
        
        
        