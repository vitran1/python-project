# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:19:36 2018

@author: Vi Tran
"""

#Code for Sales by Sub-Category Ascending

def option41():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    xl=pd . ExcelFile ("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    SalesDataMonth = SalesData
    MonthlySales = SalesDataMonth [["Sales", "Sub-Category"]]
    MonthlySalesSum = MonthlySales.groupby (by="Sub-Category").sum().sort_values( by="Sales",ascending=False)
    MonthlySalesSum = MonthlySalesSum.reset_index()
    barchart1= sns.barplot(x= "Sales", y="Sub-Category", data=MonthlySalesSum)
    barchart1.set_title("Sales by Sub-Category")
    plt.show()
    

#Code for Sales by Category
def option42():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    xl=pd . ExcelFile ("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    SalesDataMonth = SalesData
    MonthlySales = SalesDataMonth [["Sales", "Category"]]
    MonthlySalesSum = MonthlySales.groupby (by="Category").sum()
    MonthlySalesSum = MonthlySalesSum.reset_index()
    barchart1= sns.barplot(x= "Category", y="Sales", data=MonthlySalesSum)
    barchart1.set_title("Sales by Category")
    plt.show()

#Code for Sales by Region
def option43():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    xl=pd . ExcelFile ("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    SalesDataMonth = SalesData
    MonthlySales = SalesDataMonth [["Sales", "Region"]]
    MonthlySalesSum = MonthlySales.groupby (by="Region").sum()
    MonthlySalesSum = MonthlySalesSum.reset_index()
    barchart1= sns.barplot(x= "Region", y="Sales", data=MonthlySalesSum)
    barchart1.set_title("Sales by Region")
    plt.show()