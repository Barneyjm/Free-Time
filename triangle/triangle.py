# -*- coding: utf-8 -*-
"""
Triangle frequency finder
Created on Thu Jul 03 17:39:42 2014

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt


def harmonic(n, L, a, b, c):
    """
    Calculates the harmonic frequency for the given n (1, 2, 3...)
    """
    if n == 1:
        x = b + c
    elif n == 2:
        x = a + c
    else:
        x = a + b
    
    f = (n)/(2*(L-x))
    
    return f
    

    
def plot(to_plot, n, descriptor):
    x = []
    y = []
    print descriptor[0]
    
    for plottee in to_plot:
        #print plottee
        x.append(plottee[n])
        y.append(plottee[0])

    #print x.sort()
    #y.sort()
    try:
        plt.scatter(x,y)
    except: 
        plt.bar(range(len(x)), y, align='center')
        plt.xticks(arange(len(x)), x)

    plt.title(descriptor[0])
    plt.xlabel(descriptor[1])
    plt.ylabel(descriptor[2])
    
    plt.savefig(descriptor[0])
    plt.close() 

"""
L/2 > c >e L/3
c > b >e (L-c)/2
a = L-(b+c)
"""
T = 100.0
mu = 0.00072

beta = np.sqrt(T/mu)

L = 3.0

C_range = np.linspace(L/2, L/3, num=50)[1:]

first = []
second = []
third = []

for c in C_range:
    B_range = np.linspace(c, (L-c)/2, num=50)[1:]
    for b in B_range:
        a = L - (b + c)
        
        first.append((harmonic(1, L, a, b, c)*beta, a, b, c))
        second.append((harmonic(2, L, a, b, c)*beta, a, b, c))
        third.append((harmonic(3, L, a, b, c)*beta, a, b, c))
        
print len(first), len(second), len(third)

plot(first, 1, ["Frequencies First Harmonic", "Length side a", "Frequency Hz"])
plot(second, 2, ["Frequencies Second Harmonic", "Length side b", "Frequency Hz"])     
plot(third, 3, ["Frequencies Third Harmonic", "Length side c", "Frequency Hz"])


    