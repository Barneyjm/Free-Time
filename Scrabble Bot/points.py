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

def connect():
    try:
        subprocess.Popen(['C:\/mongodb\/bin\/mongod'])
    except:
        print "Failed to launch database--please try again or manually initiate."
        
    scrab_client = MongoClient()
    
    return scrab_client
    

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
        #print key
        trie.add(key, dictionary[key])
        
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

def avg_word_info(letter, dictionary):
    avg_len = 0
    avg_point = 0
    max_point = -1
    min_point = 100
    i = 0
    
    for key in dictionary.keys():
        if key.startswith(letter):
            i += 1
            avg_len += len(key)
            avg_point += dictionary[key]
            if dictionary[key] > max_point:
                max_point = dictionary[key]
            elif dictionary[key] < min_point:
                min_point = dictionary[key]
    try:        
        return avg_len/i, avg_point/i
    except ZeroDivisionError:
        return 10e-5, 10e-5
            
def words_of_length(length, dictionary):
    lengthy = dict()
    for key in dictionary.keys():
        if len(key) == length:
            lengthy[key] = dictionary[key]
            
    return lengthy
    


    
def strip_spaces(string):
    return string.replace(" ", "")
    
def keys_of_letter(dictionary, letter):
    words = dict()
    for key in dictionary.keys():
        if key.startswith(letter):
            words[key] = dictionary[key]
            
    return words
    
    

"""
try:
    db = connect()
except:
    print "already connected"    
"""


def pop_trie(string, user):
    for ch in string:
        st = string.replace(ch,'')
        while len(st) is not 0:
            user.add(ch, point_val[ch])
            print ch
            st = st[1:]
            #pop_trie(st[1:], user)
    
def total_words_of_length(dictionary, size=16):
    #size == 15 is max in given dictionary
    length_info = []
    for num in range(size+1):
        length_info.append((num, len(words_of_length(num,dictionary))))
        
    return length_info
    
def all_letter_avg_info():
    avg_info = []
    for key in point_val.keys():
        print key
        avg_info.append((key, avg_word_info(key, dictionary)[1]))
    
    plot(avg_info, ["Average Point Value of Words for each Letter", "Letter", "Average Point Value"])

    
def letter_by_letter_averages():
    for letter in alphabet:
        #print letter
        letter_words = keys_of_letter(dictionary, letter)
        #print letter_words
        plotter = []
        for length in range(2,16):
            #print length
            length_words = words_of_length(length, letter_words)
            #print length_words
            avg = avg_word_info(letter, length_words)
            plotter.append((length, avg[1]))
            #print plotter
            
        plot(plotter,["Average Point Value of Words of Length X for "+str(letter), "Length of Word", "Point Value"])
        
    
def plot(to_plot, descriptor):
    x = []
    y = []
    print descriptor[0]
    
    for plottee in to_plot:
        print plottee
        x.append(plottee[0])
        y.append(plottee[1])

    print x.sort()
    try:
        plt.bar(x,y, align='center')
    except: 
        plt.bar(range(len(x)), y, align='center')
        plt.xticks(arange(len(x)), x)

    plt.title(descriptor[0])
    plt.xlabel(descriptor[1])
    plt.ylabel(descriptor[2])
    
    plt.savefig(descriptor[0])
    plt.close()

dictionary = get_dictionary('dictionary.txt')

#print pointiest_word(dictionary)
#print score_matches(51)

#words_length_x = words_of_length(2, dictionary)

#all_lengths = total_words_of_length(dictionary)


"""
string = "If I were"
#for word in words_length_x:
string = strip_spaces(string).upper()
str_len = len(string)

t = trie_dictionary(dictionary)

#found = t.find_prefix('HEARTSZAP')
    
user = Trie()

#pop_trie(string, user)
"""
#A = keys_of_letter(dictionary, "A")
#two = words_of_length(2, A)

#plot(all_lengths, ["Lengths of Words in Scrabble Dictionary", "Characters in Word", "Words of Length x"])

