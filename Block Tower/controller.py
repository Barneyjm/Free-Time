# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:10:05 2014

Controls the various mechanics of the game like physics, 
removing blocks, and turn control.

@author: James
"""

from model import Block, Layer, Tower, Player
import numpy as np

class Game(object):
    def __init__(self, tower_height, difficulty=1):
        self.players = np.array([Player("James"), Player("Jon")])
        self.tower = Tower(tower_height)
        self.difficulty = difficulty