# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:07:59 2014

@author: James
"""
dictionary = {}

point_val = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

def score_word(line):
    """scores a word using the scrabble point system."""
    score = 0
    for letter in line:
        score += point_val[letter]
    
    return score

with open('TWL_2006_ALPHA.txt', 'r') as words:
    for line in words:
        line = line.rstrip()
        dictionary.update({line: score_word(line)})
        
print dictionary
with open('dictionary.txt', 'w') as dict_file:
    dict_file.write(str(dictionary))
        