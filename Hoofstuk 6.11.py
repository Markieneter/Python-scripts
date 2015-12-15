# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:13:51 2015

@author: Mark
"""

import random

def get_random_number(bestandd):
    
    random_number = random.choice(bestandd)
    print (random_number)
    
    
def make_quiz(random_number):
    
    return 

def main():
    bestand = open("numbers.txt")
    bestandd = bestand.read()
    bestand.close()
    get_random_number(bestandd)
    make_quiz(get_random_number(bestand))

main()


    
    