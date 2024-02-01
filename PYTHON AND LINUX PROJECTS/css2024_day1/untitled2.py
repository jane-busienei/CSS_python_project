# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:53:25 2024

@author: Neno
"""

import pandas

file4 = pandas.read_csv("housing_data.csv")
print = (file4)

#print(file4.info())

#print(df.describe())
#file4.info()
file4.describe()
#no column names
#create a new colunm for names
#column_names = ["A", "B", ...] 
#file....name = column names