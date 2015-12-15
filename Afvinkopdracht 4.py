# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:59:56 2015

@author: Mark
"""


sequentie = "GGAACG AGCGGTGTGA AAG "
Alphabet = "BDEFHIJKLMNOPQRSUVWXYZ"


def isDNA():
    for b in Alphabet:
        if b in sequentie:
            print("Error there can't be any other letters than ACGT in the sequence" )
       
            
    
       
def GC_check():
    x = sequentie.count('G')
    y = sequentie.count('C')
    z = len(sequentie)
    a = x + y
    percentage = a * 100 / z
    print(str(percentage) + " %")
   
def get_complement():        
    print (sequentie.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()) 

def main():
    isDNA()
    GC_check()
    get_complement()
main()

    
