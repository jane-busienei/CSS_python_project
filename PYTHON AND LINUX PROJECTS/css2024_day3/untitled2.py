# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:29:53 2024

@author: Neno
"""
import pandas as pd

iris_file = pd.read_csv("C:\\Users\\Neno\\PYTHON AND LINUX PROJECTS\\css2024_day2\\data_02\\iris.csv")

iris_file["class"] = iris_file["class"].str.replace("iris-", "")

