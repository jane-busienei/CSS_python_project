# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 04:36:06 2024

@author: Neno
"""

#Append & Merge
import pandas as pd
df = pd.read_csv("data_02/iris.csv")
col_names = df.columns.tolist()

df["sepal_length_sq"] = df["sepal_length"]**2
print(col_names)
# Apply the square to sepal length using a lambda function
df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)
#print(df)


#
#df2 = pd.read_csv("data_02/person_split2.csv")
#df = pd.concat([df1, df2], ignore_index=True)
#print(df)

