# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 01:47:54 2024

@author: Neno
"""

"""
Inconsistent Data Types & Names
"""
import pandas as pd

df = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())

#Extract the lower end of the age range (digits only)
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
"""
runfile('C:/Users/Neno/PYTHON AND LINUX PROJECTS/css2024_day2/Inconsistency.py', wdir='C:/Users/Neno/PYTHON AND LINUX PROJECTS/css2024_day2')
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 9 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
dtypes: float64(5), int64(2), object(2)
memory usage: 11.4+ KB
None
"""
# Step 2: Convert the new column to float
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 9 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
dtypes: float64(5), int64(2), object(2)
memory usage: 11.4+ KB
None
"""
#index column

df = pd.read_csv("data_02/time_series_data.csv")
#print(df)
"""
     Unnamed: 0        Date  Temperature
0             0  2020-01-01    27.483571
1             1  2020-01-02    24.308678
2             2  2020-01-03    28.238443
3             3  2020-01-04    32.615149
4             4  2020-01-05    23.829233
..          ...         ...          ...
361         361  2020-12-27    32.663695
362         362  2020-12-28    24.456199
363         363  2020-12-29    27.008559
364         364  2020-12-30    28.450720
365         365  2020-12-31    22.993898

[366 rows x 3 columns]
"""

df = pd.read_csv("data_02/time_series_data.csv",index_col=0)
"""
unnamed to index
To avoid the appearance of the "Unnamed: 0" column, you can either specify the existing index column from your CSV file when reading the data, or you can use the index_col parameter to explicitly specify which column you want to use as the index.
print(df)
"""
           Date  Temperature
0    2020-01-01    27.483571
1    2020-01-02    24.308678
2    2020-01-03    28.238443
3    2020-01-04    32.615149
4    2020-01-05    23.829233
..          ...          ...
361  2020-12-27    32.663695
362  2020-12-28    24.456199
363  2020-12-29    27.008559
364  2020-12-30    28.450720
365  2020-12-31    22.993898
"""
#time to date
modify, extract and filter using .str .extract .astype
"""
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')


