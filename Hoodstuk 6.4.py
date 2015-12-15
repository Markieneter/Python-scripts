# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:12:24 2015

@author: Mark
"""

def payment(loan,insurance,gas,tires,maintenace):
    total = loan + insurance + gas +tires+maintenace
    print("your monthly cost is", total)
    print("Your yearly costs are", total*12)
    




def main():
    loan = int(input("How much are your loanes? "))
    insurance = int(input("How much is your insurance? "))
    gas = int(input("How much are cost your gas use? "))
    tires = int(input("How much do you tires cost? "))
    maintenace = int(input("How much do your maintenace cost? "))
    payment(loan,insurance,gas,tires,maintenace)
   
main()