# coding: utf-8
import glob


def donne_moi_ton_nom():
    return "Olivier"

def ageplus1(a):
    return a+1

def ajoute_deux(a):
    return a+2

import os
import glob
f = "C:\projet"
print(glob.glob("C:\projet\*.txt"))
for path, dirs, files in os.walk(f):
    for f in path :
        print(f)
