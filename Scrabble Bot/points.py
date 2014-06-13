# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:07:59 2014
Reads a text file for the official scrabble dictionary and assigns point values to those words

@author: James
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import ast
from trie import Trie
from pymongo import MongoClient
import subprocess


point_val = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
alphabet = set(point_val.keys())

try:
    subprocess.Popen(['C:\/mongodb\/bin\/mongod'])
except:
    print "Failed to launch database--please try again or manually initiate."
    
scrab_client = MongoClient()
    

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
            
def store_dict(dictionary):       
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

def trie_dictionary(dictionary):
    trie = Trie()
    
    for key in dictionary.keys():
        trie[key] = True
        
    return trie
    
def pointiest_word(dictionary):
    return max(dictionary, key=dictionary.get)

def pointless_word(self, dictionary):
    return min(dictionary, key=dictionary.get)

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
            
def words_of_length(length, dictionary):
    lengthy = []
    for key in dictionary.keys():
        if len(key) == length:
            lengthy.append(key)
            
    return lengthy
    
dictionary = get_dictionary('dictionary.txt')

print pointiest_word(dictionary)
print score_matches(51)
avg_info = []
for key in point_val.keys():
    #print key
    avg_info.append((key, avg_word_info(key)))

def plot(to_plot):
    x = range(1,27)
    y = []
    for letter in to_plot:
        y.append(letter[1][1])
    
    plt.bar(x, y)

words_length_x = words_of_length(2, dictionary)


def strip_spaces(string):
    return string.replace(" ", "")


string = "If I were"
#for word in words_length_x:
string = strip_spaces(string)
str_len = len(string)

for ch in string.upper():
    if ch in alphabet:
        print ch
        
        
    
    
    
    
    
    
