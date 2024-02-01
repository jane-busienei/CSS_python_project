# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 01:59:34 2024

@author: Neno
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("poker_2016_09_27.csv", names = ["Time", "Num", "X", "Y", "Z"])
df['Time'] = pd.to_datetime(df['Time'], format = '%H:%M:%S')
plt.plot(df['Time'], df['X'], label = "x")