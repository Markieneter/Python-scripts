# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:46:36 2015

@author: Mark
"""
import sys


def bestand():
    # Functie om het bestand te openen
    try:
        # Normale script
        bestand = open("Afvink5.fa")
        # opent het bestand afvink.fa
        seq = bestand.readlines()
        # leest alle regels van het bestand en noemt het seq
        bestand.close()
        # sluit het bestand
        
        return seq
        # Return seq, zodat het weer opgehaald kan worden in een andere functie gebruikt kan worden
    except IOError:
        # als er een input of output error is print dan:
        print("Error wrong input or output")

    
def titel_check(seq):
    # Functie voor het vinden van nodige informatie
    try:
        # Normale script
        x = str(input("What enzym do you want to use? "))
        # vraagt naar enzym naam of nummer 
        for sequentie in seq:
            # Loop voor het bestand
            if ">" in sequentie and x in sequentie:
                # als > en x in het bestand zit print :
                print(sequentie)
    except KeyboardInterrupt:
         # als er een keyboard error is print dan:
        print("Error")
        
        
    

def main(argv=None):
   if argv is None:
       argv = sys.argv


   bstnd = bestand()
   titel_check(bstnd)


if __name__ == "__main__":
    sys.exit(main())



