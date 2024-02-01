# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 04:55:22 2024

@author: Neno
"""
import pandas as pd

df1 = pd.read_csv("data_02/person_work.csv")
df2 = pd.read_csv("data_02/person_education.csv")

df_merge_inner = pd.merge(df1,df2,on="id")
print(df_merge_inner.info())