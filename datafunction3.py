# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:04:04 2018

@author: Dan
"""
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
#pd.set_option('display.precision',2)
pd.options.display.float_format = '{:,.2f}'.format
##########################################################
    
xl = pd.ExcelFile("FA18SalesData.xlsx")
SalesData = xl.parse("Orders")
    

def option31():
        
    sub_profit = SalesData[["Sub-Category", "Quantity", "Profit"]].copy()
    sub_group_profit = sub_profit.groupby(by = "Sub-Category").sum().sort_values(by = "Profit", ascending = False)
    sub_group_profit = sub_group_profit.reset_index()
    print(sub_group_profit)
    
def option32(x):
    select = True
    
    category_profit = SalesData[["Product Name", "Quantity", "Profit"]].copy()
    category_loc_profit = category_profit.loc[SalesData["Sub-Category"] == x].copy()
    new_cat_profit = category_loc_profit.groupby(by = "Product Name").sum().sort_values(by= "Profit", ascending = False)
    new_cat_profit = new_cat_profit.reset_index()
    
    while select:
        choice = input("What percentage of the products in this sub-category would you like to see (Enter a whole number from 0-100 to see all)?  ")
        if choice == '':
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this Sub-Category and press ENTER.")
            continue
        try:
            choice = int(choice)
        except ValueError:
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this Sub-Category and press ENTER.")
            continue
        if choice >= 0 and choice <= 100:
            pass
        else:
            print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this Sub-Category and press ENTER.")
            continue
        choice = float(choice / 100)
        top_p = int(new_cat_profit.shape[0] * choice)
        print(new_cat_profit.head(top_p))
        tot = new_cat_profit['Profit'].sum()
        print("\nThe profit for the", x, "sub-category is: $", '{0:,.2f}'.format(tot))
        select = False
    
def option33():
    select = True

    whole = SalesData[["Sub-Category", "Sales", "Quantity", "Discount", "Profit"]].copy()
    whole['Price Per Unit'] = (whole['Sales']/ (1 - whole['Discount'])) / whole['Quantity']
    #whole['Cost Per Unit'] = (whole['Sales'] - whole['Profit']) / whole['Quantity']
    
    category_gross = SalesData[["Product Name", "Sub-Category", "Quantity"]].copy()
    category_gross['Gross Sales'] = (category_gross['Quantity']/4) * whole['Price Per Unit']
    new_gross = category_gross.groupby(by = "Product Name").sum().sort_values(by = "Gross Sales", ascending = False)
    new_gross['Sum'] = new_gross['Gross Sales'].cumsum()
    tot_rev = new_gross['Gross Sales'].sum()
    new_gross['Class'] = ''
    new_gross.loc[new_gross.Sum < (tot_rev *.8), 'Class'] = 'A'
    new_gross.loc[(new_gross.Sum > (tot_rev *.8)) & (new_gross.Sum < (tot_rev *.95)), 'Class'] = 'B'
    new_gross.loc[new_gross.Sum > (tot_rev *.95), 'Class'] = 'C'
    new_gross = new_gross.reset_index()
    
    while select:
        option = input("1. View A-class Products\n2. View B-Class Products\n3. View C-Class Products\n4. View All\n5. Return to previous menu\nOPTION: ")
        if option == "":
            print("This field cannot be left blank\n")    
        elif option == "1": 
            select2 = True
            while select2:
                choice = input("What percentage of the products in this classification would you like to see (Enter 100 to see all)? ")
                if choice == '':
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                try:
                    choice = int(choice)
                except ValueError:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                if choice >= 0 and choice <= 100:
                    pass
                else:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                choice = float(choice / 100)
                final_gross = new_gross[["Product Name", "Quantity", "Gross Sales", "Class"]]
                selection = final_gross.loc[final_gross["Class"] == 'A']
                top_p = int(selection.shape[0] * choice)
                print(selection.head(top_p))
                tot = selection['Gross Sales'].sum()
                print("\nThe annual gross sales for this classification is: $", '{0:,.2f}'.format(tot))
                select2 = False
            select = False
        elif option == "2":
            select2 = True
            while select2:
                choice = input("What percentage of the products in this classification would you like to see (Enter 100 to see all)? ")
                if choice == '':
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                try:
                    choice = int(choice)
                except ValueError:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                if choice >= 0 and choice <= 100:
                    pass
                else:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                choice = float(choice / 100)
                final_gross = new_gross[["Product Name", "Quantity", "Gross Sales", "Class"]]
                selection = final_gross.loc[final_gross["Class"] == 'B']
                top_p = int(selection.shape[0] * choice)
                print(selection.head(top_p))
                tot = selection['Gross Sales'].sum()
                print("\nThe annual gross sales for this classification is: $", '{0:,.2f}'.format(tot))
                select2 = False
            select = False
        elif option == "3":
            select2 = True
            while select2:
                choice = input("What percentage of the products in this classification would you like to see (Enter 100 to see all)? ")
                if choice == '':
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                try:
                    choice = int(choice)
                except ValueError:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                if choice >= 0 and choice <= 100:
                    pass
                else:
                    print("Error Message: Invalid input... please enter a whole number from 0-100 to see the percentage of products in this classification and press ENTER.")
                    continue
                choice = float(choice / 100)
                final_gross = new_gross[["Product Name", "Quantity", "Gross Sales", "Class"]]
                selection = final_gross.loc[final_gross["Class"] == 'C']
                top_p = int(selection.shape[0] * choice)
                print(selection.head(top_p))
                tot = selection['Gross Sales'].sum()
                print("\nThe annual gross sales for this classification is: $", '{0:,.2f}'.format(tot))
                select2 = False
            select = False
        elif option == "4":
            final_gross = new_gross[["Product Name", "Quantity", "Gross Sales", "Class"]]
            print(final_gross)
            tot = final_gross['Gross Sales'].sum()
            print("\nThe annual gross sales for this classification is: $", '{0:,.2f}'.format(tot))
            select = False
        elif option == "5":
            return
        else:
             print("Error Message: Invalid input... please enter a numerical value for the association task you wish to perform and press ENTER. Otherwise Select 5 to return to previous menu.")
             
def option34():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders", index_col=0)
    
    
    sub_cat = SalesData["Sub-Category"]
    sub_cat_group = sub_cat.drop_duplicates().reset_index().drop(columns='Row ID')
    print(sub_cat_group)
    
    select = True
    while select:
        choice = input("These are your Sub-Categories, please enter the number that corresponds to the Sub-Category you would like to see: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Error Message: Invalid input... please enter the number that corresponds with the Sub-Category in which you would like see and press ENTER.")
            continue
        if choice >= 0 and choice <= 16:
            pass
        else:
            print("Error Message: Invalid input... please enter a whole number from 0-16 to see the sub-categories of products in this and press ENTER.")
            continue
        choice = sub_cat_group.loc[choice]['Sub-Category']
        select = False
        return choice
