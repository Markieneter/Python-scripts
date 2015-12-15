# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:01:58 2015

@author: Mark
"""
def calc_state_sale(purchase):
    print("You have to pay:",purchase * 0.025, "state tax ")

def calc_county_sale(purchase):
    print("You also have to pay:",purchase * 0.05, "county tax")
    
def calc_
    
def main():
    purchase = int(input("How much did you purchase? "))
    calc_state_sale(purchase)
    calc_county_sale(purchase)
main()