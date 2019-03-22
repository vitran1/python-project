# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:22:50 2018

@author: Vi
"""
##########################################################
    #DATA SET FOR OPTION 1-1
import percent

def option111():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    
    top_frequent = SalesData["Customer Name"].value_counts()
    percent.percentage(top_frequent)
    

def option112():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")

    top_frequent = SalesData["Segment"].value_counts()
    print (top_frequent.head(10))
    

def option113():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")

    top_frequent = SalesData["City"].value_counts()
    percent.percentage(top_frequent)

##########################################################
    #DATA SET FOR OPTION 1-2
def option121():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    OrdersOnlyData = xl.parse("Orders")
    
    prod_prof_col = OrdersOnlyData[["Customer Name","Profit"]]     
    prod_prof = prod_prof_col.groupby(by="Customer Name").sum().sort_values(by="Profit", ascending = False)
    percent.percentage(prod_prof)


def option122():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    
    seg_prof_col = SalesData[["Segment","Profit"]]     
    seg_prof = seg_prof_col.groupby(by="Segment").sum().sort_values(by="Profit", ascending = False)
    print (seg_prof.head(10))

    
def option123():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    OrdersOnlyData = xl.parse("Orders")
    
    city_prof_col = OrdersOnlyData[["City","Profit"]]     
    city_prof = city_prof_col.groupby(by="City").sum().sort_values(by="Profit", ascending = False)
    percent.percentage(city_prof)
    
#############################################################
