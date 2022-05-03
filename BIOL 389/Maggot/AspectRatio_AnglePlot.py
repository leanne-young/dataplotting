#Plot AR and Angles of Larvae through time
#Data from FIJI -> JMP analysis

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np

#import csv
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Maggots\FedLarva.csv")
#data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Maggots\StarvedLarva.csv")

# make dataframe from data
df = pd.DataFrame(data, columns=["Time", "AR", "Angle"])

x = df['Time']
#y = df['AR']
y = df["Angle"]

#Line plots ------------------------------
plt.figure()
plt.plot(x, y, color="deepskyblue") #changed colors for each condition

#customizing plot -------------------------------
plt.suptitle('Adjusted Angle of Fed Larva by Time', fontsize=25, fontfamily='fantasy')
plt.ylabel('Adjusted Angle', fontsize=15, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel('Time (s)', fontsize=15, fontfamily='sans-serif', weight="bold") #customize x axis label
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
#legend_elements = [Line2D([0], [0], marker='s', color='w', label='Control',
#                          markerfacecolor='dodgerblue', markersize=10),
#                   Line2D([0], [0], marker='s', color='w', label='TEA Wash-in',
#                          markerfacecolor='orangered', markersize=10)]

#plt.legend(handles=legend_elements, loc="upper right")

#set size
fig = plt.gcf()
fig.set_size_inches(50,6)
 
# display plot
plt.show()
