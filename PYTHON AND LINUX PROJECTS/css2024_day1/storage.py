# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 04:40:39 2024

@author: Neno
"""

"""
1. lists
2. dictionaries
data frames specific to pandas
"""
import pandas as pd

file = pd.read_csv("country_data.csv")

#print(file)
age1 = 30
age2 = 25
age3 = 29
age4 = 46

age = [30, 25, 29, 46]
print(age)
age.insert(0,100)
print(age[1])
print("minimum age is:", min(age))
print("maximum age is:", max(age))
print("sum age is:", sum(age))
print("length is:", len(age))
avg = sum(age)/len(age)
print("average age is:", avg)

"""
25
[30, 25, 29, 46]
30
minimum age is: 25
maximum age is: 100
sum age is: 230
length is: 5
average age is: 46.0
"""
#gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
"""
M
M
F
M
"""
gender.append("F")
print(gender)
"""
['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'M', 'F']

"""

"""
DICTIONARY- key:vale pairs
"""
mammals = {"cat": "a cute cat", "lion": "a king of the jungle",
           "monkey": "half human"}
print(mammals["cat"])

fruit_sizes = {
    'fruits':"banana", "mango", "pineapple", "apple", "orange"
    
    'sizes': 25, 30, 54, 57, 67
    }
    
"""
DATAFRAMES
"""
import pandas as pd

df = pd.DataFrame('fruit')

print(df['sizes'].min())

print(df['sizes'].mean())

print(df[df["sizes"]> 20])
