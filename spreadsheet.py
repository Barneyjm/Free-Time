# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 15:59:04 2014

@author: james
"""

class Spreadsheet(object):
    def __init__(self, x=50, y=50):
        self.sheet = [[Cell(i,i) for i in xrange(x)] for i in xrange(y)]
    
class Cell(object):
    def __init__(self, xid, yid):
        self._contents = None
        self.ID = str(xid) + str(yid)
        
        self._height = 10.0
        self._width = 40.0
        self.neighbors = {"top": None, "bottom": None, "left": None, "right": None}
        
    def set_contents(self, content):
        self._contents = content
        
    def get_contents(self):
        return self._contents
        
    def set_height(self, height):
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_neighbor(self, side, neighbor):
        self.neighbors[side] = neighbor
        
    def get_neighbor(self, side, neighbor):
        return neighbor[side]
        
if __name__ == '__main__':
    sheet = Spreadsheet()
    
