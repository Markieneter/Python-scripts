# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:26:09 2015

@author: Mark
"""
import random
New_list = []
def main():
    try:
        bestand = open("Galgje.txt")
        
        append(bestand)
        #guess(Word_string)
    except IOError:
        print("Input, Ouput error, something went wrong with opening the file")
   
        
def append(bestand):
    for x in bestand:
        regel = bestand.readline()
        woord = regel.split()
        New_list.append(woord)
    
    print(New_list)
    Word_string = New_list[random.randint(0,len(New_list))]
    print(type(Word_string))
    Word_string = Word_string.replace("'","").replace("[","").replace("]","")
    return Word_string
    
def underscore_list(Word_string):
    guess_list = ["_"] * len(Word_string)
    print(guess_list)
    

def guess_word(Word_string):
    for x in Word_string:
        if x in Word_string:
            
            return
            
    
            
        
        
        
        
        
main()
        
    
    