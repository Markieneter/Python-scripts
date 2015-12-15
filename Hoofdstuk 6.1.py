# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:57:39 2015

@author: Mark
"""

def get_kilometers():
    Amount_of_km = int(input("How much KM did you travel?" ))
    print("The amount of miles traveld is", Amount_of_km * 0.6214 )
    
    
def main():
    get_kilometers()
main()