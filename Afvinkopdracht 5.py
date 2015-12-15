# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:46:36 2015

@author: Mark
"""

try:
    bestand = open("Afvink5.fa")
    seq = bestand.readlines()
    print(seq)
except IOError:
    print("kaas")