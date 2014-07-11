# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 15:59:04 2014

@author: james
"""
from pprint import pprint

class Spreadsheet(object):
    def __init__(self, x=3, y=3):
        self.sheet_num = 0
        self.sheets = {}
        self.sheets[self.sheet_num] = self.make_sheet(x, y)

    def make_sheet(self, x, y):
        self.sheet_num += 1
        return [[Cell(i,i) for i in xrange(x)] for i in xrange(y)]        

    def get_row(self, x, sheet=1):
        return self.sheets[sheet][x]

    def get_col(self, y, sheet=1):
        return [row[y] for row in self.sheets[sheet] ]

    def get_cell_content(self, x, y, sheet=1):
        return self.sheets[sheet][x][y].get_content()

    def set_cell_content(self, x, y, content, sheet=1):
        self.sheets[sheet][x][y].set_content(content)

    def mult_cells(self, x1, y1, x2, y2, sheet=1):
        return self.get_cell_content(x1,y1)*self.get_cell_content(x2,y2)
        
        
class Cell(object):
    def __init__(self, xid, yid):
        self._content = None
        self.ID = str(xid) + str(yid)
        
        self._height = 10.0
        self._width = 40.0
        self.neighbors = {"top": None, "bottom": None, "left": None, "right": None}

    def __repr__(self):
        return str(self.get_content())
        
    def set_content(self, content):
        self._content = content
        
    def get_content(self):
        return self._content
        
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

    pprint(sheet.sheets[1])
    sheet.set_cell_content(0,0, 5)
    sheet.set_cell_content(0,1, 3)
    pprint(sheet.sheets[1])
    
    print sheet.mult_cells(0,0,0,1)
    
   
