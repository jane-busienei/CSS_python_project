# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:42:03 2024

@author: Neno
"""

import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

astrofile = pd.read_csv(url)
plt.plot(astrofile)