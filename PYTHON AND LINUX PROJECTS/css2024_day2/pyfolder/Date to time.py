# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 02:38:20 2024

@author: Neno
"""
import pandas as pd

df = pd.read_csv("data_02/patient_data_dates.csv", index_col = 0)


df.drop(index=26, inplace = True)
df["Date"] = pd.to_datetime(df["Date"])

print(df.info())
"""
Index: 31 entries, 0 to 31
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype         
---  ------    --------------  -----         
 0   Duration  31 non-null     int64         
 1   Date      30 non-null     datetime64[ns]
 2   Pulse     31 non-null     int64         
 3   Maxpulse  31 non-null     int64         
 4   Calories  29 non-null     float64       
dtypes: datetime64[ns](1), float64(1), int64(3)
memory usage: 1.5 KB
None
"""
