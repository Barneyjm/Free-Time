# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:07:59 2014
Reads a text file for the official scrabble dictionary and assigns point values to those words

@author: James
"""
import numpy
import os
import ast

point_val = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

def score_word(line):
    """scores a word using the scrabble point system."""
    score = 0
    for letter in line:
        score += point_val[letter]
    
    return score
    
def setup():
    dictionary = {}

    with open('TWL_2006_ALPHA.txt', 'r') as words:
        for line in words:
            line = line.rstrip()
            dictionary.update({line: score_word(line)})
            
    return dictionary
            
def store_dict():       
    #print dictionary
    with open('dictionary.txt', 'w') as dict_file:
        dict_file.write(str(dictionary))
        
def get_dictionary(fname):
    if os.path.isfile(fname):
        with open(fname, 'r') as f:
            print("Found existing dictionary.")
            dictionary = ast.literal_eval(f.read())
            
    else:
        dictionary = setup() 
        
    return dictionary

def pointiest_word():
    return max(dictionary, key=dictionary.get)

def score_matches(score):
    for key in dictionary.keys():
        if dictionary[key] >= score:
            return key
    else: return "No word with that score found"

def avg_word_info(letter):
    avg_len = 0
    avg_point = 0
    i = 0
    for key in dictionary.keys():
        if key.startswith(letter):
            i += 1
            avg_len += len(key)
            avg_point += dictionary[key]
            
    return avg_len/i, avg_point/i
            
            
    
dictionary = get_dictionary('dictionary.txt')

print pointiest_word()
print score_matches(51)
avg_info = []
for key in point_val.keys():
    #print key
    avg_info.append((key, avg_word_info(key)))
    
print avg_info
