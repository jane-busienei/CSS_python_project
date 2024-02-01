# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 02:38:20 2024

@author: Neno
"""
import pandas as pd

df = pd.read_csv("data_02/patient_data_dates.csv", index_col = 0)


df.drop(index=26, inplace = True)
df["Date"] = pd.to_datetime(df["Date"])

#print(df.info())
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
avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace = True)
df.dropna(inplace = True)

#replace an outliers
df = df.reset_index(drop=True)
df['Duration'] = df['Duration'].replace([450], 50)
print(df)
"""
    Duration       Date  Pulse  Maxpulse    Calories
0         60 2020-12-01    110       130  409.100000
1         60 2020-12-02    117       145  479.000000
2         60 2020-12-03    103       135  340.000000
3         45 2020-12-04    109       175  282.400000
4         45 2020-12-05    117       148  406.000000
5         60 2020-12-06    102       127  300.000000
6         60 2020-12-07    110       136  374.000000
7         50 2020-12-08    104       134  253.300000
8         30 2020-12-09    109       133  195.100000
9         60 2020-12-10     98       124  269.000000
10        60 2020-12-11    103       147  329.300000
11        60 2020-12-12    100       120  250.700000
12        60 2020-12-12    100       120  250.700000
13        60 2020-12-13    106       128  345.300000
14        60 2020-12-14    104       132  379.300000
15        60 2020-12-15     98       123  275.000000
16        60 2020-12-16     98       120  215.200000
17        60 2020-12-17    100       120  300.000000
18        45 2020-12-18     90       112  306.565517
19        60 2020-12-19    103       123  323.000000
20        45 2020-12-20     97       125  243.000000
21        60 2020-12-21    108       131  364.200000
22        60 2020-12-23    130       101  300.000000
23        45 2020-12-24    105       132  246.000000
24        60 2020-12-25    102       126  334.500000
25        60 2020-12-27     92       118  241.000000
26        60 2020-12-28    103       132  306.565517
27        60 2020-12-29    100       132  280.000000
28        60 2020-12-30    102       129  380.300000
29        60 2020-12-31     92       115  243.000000
"""
