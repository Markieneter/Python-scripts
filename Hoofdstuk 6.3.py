# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:41:26 2015

@author: Mark
"""



def get_insurance(price):
    print("The insurance cost", price * 0.8, "euro")
    
def main():
    price = int(input("How much does it cost to replace your house? "))
    get_insurance(price)
    
main()