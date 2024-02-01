# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:42:45 2024

@author: Neno
"""
import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")

#print(df)
"""
    Unnamed: 0  Age Gender       Country
0            0   39      M  South Africa
1            1   25      M      Botswana
2            2   29      F  South Africa
3            3   46      M  South Africa
4            4   22      F         Kenya
5            5   35      F    Mozambique
6            6   22      F       Lesotho
7            7   49      M         Kenya
8            8   30      M         Kenya
9            9   40      F         Egypt
10          10   30      M         Sudan
"""


"""
CSV to TXT
"""
file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

#print(file)
"""
 Landcover Type Select Crop Type  ...          X          Y
0            crop           tomato  ...  30.146589 -22.894748
1            crop           tomato  ...  30.146506 -22.894734
2            crop           tomato  ...  30.146305 -22.894717
3            crop           tomato  ...  30.146147 -22.894691
4            crop           tomato  ...  30.146070 -22.894575
..            ...              ...  ...        ...        ...
87           soil             soil  ...  30.145931 -22.894080
88           soil             soil  ...  30.145929 -22.893918
89           soil             soil  ...  30.146283 -22.893956
90           soil             soil  ...  30.146436 -22.893789
91           soil             soil  ...  30.145790 -22.893725

[92 rows x 11 columns]
"""
#Reading Json file
file2 = pd.read_json("data_02/student_data.json")

#print(file2)

"""
   id                   field  ... amount_of_students  campus
0   1        Computer Science  ...               3000       A
1   2  Biomedical Engineering  ...               4000       B
2   3                 Physics  ...               2000       A
3   4             Mathematics  ...               3100       C

[4 rows x 5 columns]
"""
#Reading xml file
file3 = pd.read_excel("data_02/residentdoctors.xlsx")
#print(file3)


