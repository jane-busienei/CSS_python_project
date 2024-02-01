# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:21:22 2024

@author: Neno
"""

import plotly_express as px
#import plotly as pt
"""
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color="species")
fig.show()

"""
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]

temp = [180, 200, 220, 240, 260]


fig = px.scatter(x = temp, y = react_conv)

fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")