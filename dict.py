#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:05:55 2020

@author: sshanto


def fn1(x):
    print ("One "+str(x))

def fn2():
    print ("Two")

def fn3():
    print ("Three")

fndict = {"A": fn1, "B": fn2, "C": fn3}

keynames = ["A", "B", "C"]

fndict[keynames[0]](4)
"""
import random



x = ["skip", "reverse", "draw 2"]
z = []


for i in range(10):
    y = random.randint(0,2)
    z.append(x[y])

def sortd(z):
        x = ["skip", "reverse", "draw 2"]
        sindex = []
        dindex = []
        rindex = []
        for i in range(len(z)):
            if z[i] == x[0]:
                sindex.append([z[i]])
            elif z[i] == x[1]:
                dindex.append([z[i]])
            else:
                rindex.append([z[i]])
        zsort = sindex + dindex + rindex
        print(zsort)
        print()

y = ["draw 2"]
sortd(y)


sx = ["skip", "reverse", "draw 2"]

while len(sx) != 0:
    print(sx.pop(0))

"""
print(z)
print("\n\n")
zsort = sindex + dindex + rindex
print(zsort)
"""



