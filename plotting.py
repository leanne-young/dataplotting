#Plot APs from clampfit

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np

#import csv
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\ControlvTEA.csv")

# make dataframe from data
df = pd.DataFrame(data, columns=["Time", "Control", "TEA"])

#plotting subsets ------------------------------
#plotting each line separately to manually change colors and properties easily
x = df['Time']
y1 = df['Control']
y2 = df['TEA']

#Line plots ------------------------------
plt.plot(x,y1, color="blue", label="Control")
plt.plot(x,y2, color="red", label="TEA Wash-in")

#customizing plot -------------------------------S
plt.suptitle('Action Potential of Control vs. TEA Wash-In', fontsize=20, fontfamily='fantasy')
plt.ylabel('Voltage (mV)', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel('Time (ms)', fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='Control',
                          markerfacecolor='dodgerblue', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='TEA Wash-in',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper right")
#plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.spring(np.linspace(0, 1, 6)))) #set order of color cycle

#add annotations (arrows and comments) to the plot
#plt.annotate('A',
#    xy=(260, 743), xycoords='data',
#    xytext=(20, 33), textcoords='offset points',
#    arrowprops=dict(facecolor='black', shrink=0.02),
#    horizontalalignment='right', verticalalignment='bottom')

#plt.annotate('B',
#    xy=(153, 1050), xycoords='data',
#    xytext=(40, -10), textcoords='offset points',
#    arrowprops=dict(facecolor='black', shrink=0.02),
#    horizontalalignment='right', verticalalignment='bottom')

 
# display plot
plt.show()