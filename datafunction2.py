# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:13:57 2018

@author: Dan
"""

import percent
##########################################################
    

def option221():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    pd.set_option('display.max_colwidth', -1)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.max_rows', 500)
    #pd.set_option('display.precision',2)
    pd.options.display.float_format = '{:,.2f}'.format
    SalesData = xl.parse("Orders", index_col = 0)
    
    whole = SalesData[["Product ID", "Product Name", "Category", "Sub-Category", "Quantity", "Sales", "Discount", "Profit"]].copy()
    whole = whole.drop_duplicates()
    whole['Price Per Unit'] = (whole['Sales']/ (1 - whole['Discount'])) / whole['Quantity']
    whole['Cost Per Unit'] = (whole['Sales'] - whole['Profit']) / whole['Quantity']
    whole['Break Even Point'] = 1 - (whole['Cost Per Unit'] / whole['Price Per Unit'])
    
    new = whole[["Product ID", "Product Name", "Category", "Sub-Category", "Price Per Unit", "Break Even Point"]]
    #new.set_index("Product ID", inplace = True)
    new = new.reset_index().drop(columns='Row ID')
    

    select = True
    while select:
        #prod_id = 'FUR-BO-10001798' 
        prod_id = input("Please enter the Product ID and press ENTER (example: FUR-BO-10001798): ")
        try:
            id_loc = new.loc[new['Product ID'] == prod_id]
            id_num = id_loc.iloc[0, 0]
        except IndexError:
            print("The Product ID you entered was not found, please try again.")
            continue
            
        print(id_loc.head(1))
        select = False
        
def option222():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    pd.set_option('display.max_colwidth', -1)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.max_rows', 500)
    #pd.set_option('display.precision',2)
    pd.options.display.float_format = '{:,.2f}'.format
    SalesData = xl.parse("Orders", index_col = 0)
    
    whole = SalesData[["Product ID", "Product Name", "Category", "Sub-Category", "Quantity", "Sales", "Discount", "Profit"]].copy()
    whole = whole.drop_duplicates()
    whole['Price Per Unit'] = (whole['Sales']/ (1 - whole['Discount'])) / whole['Quantity']
    whole['Cost Per Unit'] = (whole['Sales'] - whole['Profit']) / whole['Quantity']
    whole['Break Even Point'] = 1 - (whole['Cost Per Unit'] / whole['Price Per Unit'])
    
    new = whole[["Product ID", "Product Name", "Category", "Sub-Category", "Quantity", "Profit", "Discount", "Break Even Point"]]
#    new.set_index("Product ID", inplace = True)
    new2 = new.sort_values( by = 'Profit').reset_index().drop(columns='Row ID')
    print(new2.head(100))
    
    
    
def option211():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    OrdersOnlyData = xl.parse("Orders")
    
    prod_prof_col = OrdersOnlyData[["Product Name", "Profit"]]     
    prod_prof = prod_prof_col.groupby(by="Product Name").sum().sort_values(by="Profit", ascending = True)
    percent.percentage(prod_prof)
    
