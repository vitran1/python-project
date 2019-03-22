# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:15:29 2018

@author: Vi Tran
"""
def percentage(x):
    select = True
    while select:
        choice = input("What percentage would you like to see (Enter a whole number from 0-100)?  ")
        if choice == '':
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage and press ENTER.")
            continue
        try:
            choice = int(choice)
        except ValueError:
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage and press ENTER.")
            continue
        if choice >= 0 and choice <= 100:
            pass
        else:
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage and press ENTER.")
            continue
        choice = float(choice / 100)
        top_p = int(x.shape[0] * choice)
        print(x.head(top_p))
        select = False