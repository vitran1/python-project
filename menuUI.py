# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:57:11 2018

@author: vit
"""

invalid = "Error Message: Invalid input... Please enter a valid number option."
blankerror = "This field cannot be left blank\n"
lines = "="*25
import datafunction1
import datafunction2
import datafunction3
import datafunction4
import registration
import Login

def mainmenu():
    print("Welcome to the MAIN MENU \n \nPlease enter the number you wish to perform.")
    menuoption = input("1. View top customers for rewards program. \n2. Production Discontinuation & Break-even analysis based on discounts. \n3. View top subcategories to focus on. \n4. View charts for Sales \n5. Register a new user. \n6. Logout and return to login screen. \n0. Exit\nOPTION:").strip()
    if menuoption =="":
        print(blankerror)
        mainmenu()
    elif menuoption =="1":
        rewardprog()
    elif menuoption =="2":
        discontinuityprog()
    elif menuoption =="3":
        subcatmenu1()
    elif menuoption =="4":
        chartmenu1()
    elif menuoption =="5":
        registration.registration()
    elif menuoption =="6":
        Login.login()
    elif menuoption =="0":
        SystemExit(0)
    else:
        print(invalid)
        mainmenu()

##### Menu Function for Option 1
def rewardprog():
    rewardp = input("1. View top customer orders based on frequency.\n2. View top customer orders based on profit.\n3. Return to Main Menu.\nOPTION: ").strip()
    
    if rewardp =="":
        print(blankerror)
        rewardprog()
    elif rewardp =="1":
        frequencymenu1()
    elif rewardp =="2":
        profitmenu1()
    elif rewardp =="3":
        mainmenu()
    else:
        print(invalid)
        rewardprog()
        
def frequencymenu1():
    freqoption = input("1. Frequency by Customer Name\n2. Frequency by Segments (Consumers, Corporate, Home Office)\n3. Frequency by City\n4. Return to previous menu\nOPTION: ").strip()

    if freqoption =="":
        print(blankerror)
        frequencymenu1()
    elif freqoption =="1":
        print(lines)
        datafunction1.option111()
        frequencymenu1()
    elif freqoption =="2":
        print(lines)
        datafunction1.option112()
        frequencymenu1()
    elif freqoption =="3":
        print(lines)
        datafunction1.option113()
        frequencymenu1()
    elif freqoption =="4":
        rewardprog()
    else:
        print(invalid)
        frequencymenu1()

def profitmenu1():
    profoption = input("1. Profit by Customer Name\n2. Profit by Segments (Consumers, Corporate, Home Office)\n3. Profit by City\n4. Return to previous menu\nOPTION: ").strip()

    if profoption =="":
        print(blankerror)
        profitmenu1()
    elif profoption =="1":
        print(lines)
        datafunction1.option121()
        profitmenu1()
    elif profoption =="2":
        print(lines)
        datafunction1.option122()
        profitmenu1()
    elif profoption =="3":
        print(lines)
        datafunction1.option123()
        profitmenu1()
    elif profoption =="4":
        rewardprog()
    else:
        print(invalid)
        profitmenu1()

################ END
        
################ Menu Function for option 2

def discontinuityprog():
    disconprog = input("1. Product discontinuation analysis based on profit. \n2. Least profitable sales with Break-even analysis\n3. Break-even point based on ProductID. \n4. Return to Main Menu.\nOPTION: ").strip()
    
    if disconprog =="":
        print(blankerror)
        discontinuityprog()
    elif disconprog =="1":
        datafunction2.option211()
        discontinuityprog()
    elif disconprog =="2":
        datafunction2.option222()
        discontinuityprog()
    elif disconprog =="3":
        datafunction2.option221()
        discontinuityprog()
    elif disconprog =="4":
        mainmenu()
    else:
        print(invalid)
        discontinuityprog()
        
    
################ END

################ Menu Function for option 3
        
def subcatmenu1():
    catoption = input("1. Profit by Sub-Category\n2. Profit by Specific Sub-Category\n3. ABC Classification of Product Catalog\n4. Return to Main Menu\nOPTION: ").strip()
    if catoption =="":
        print("This field cannot be left blank\n")
        subcatmenu1()
    elif catoption =="1":
        print(lines)
        datafunction3.option31()
        subcatmenu1()
    elif catoption =="2":
        print(lines)
        from datafunction3 import option34, option32
        x = option34()
        option32(x)
        subcatmenu1()
    elif catoption =="3":
        print(lines)
        datafunction3.option33()
        subcatmenu1()
    elif catoption =="4":
        mainmenu()
    else:
        print(invalid)
        subcatmenu1()
    
    
################ END
        
################ Menu Function for option 4
        
def chartmenu1():
    chartoption = input("1. Chart view of Top Sales by Sub-Category\n2. Chart view of Top Sales by Category\n3. Chart view of Top Sales by Region\n4. Return to Main Menu\nOPTION: ").strip()
    if chartoption =="":
        print("This field cannot be left blank\n")
        chartmenu1()
    elif chartoption =="1":
        print(lines)
        datafunction4.option41()
        chartmenu1()
    elif chartoption =="2":
        print(lines)
        datafunction4.option42()
        chartmenu1()
    elif chartoption =="3":
        print(lines)
        datafunction4.option43()
        chartmenu1()
    elif chartoption =="4":
        mainmenu()
    else:
        print(invalid)
        chartmenu1()



















