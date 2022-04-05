#Plot APs from clampfit

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np

#import csv's
data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Leech\IV_RealRecording.csv")

# make dataframes from data
df = pd.DataFrame(data, columns=["V", "I"])

#calculating values ------------------------------
x = df['I']
y = df['V']
coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)
slope = coef[0]

#Line plots ------------------------------
plt.figure()
plt.plot(x, y, marker='o', color="paleturquoise")
plt.plot(x, poly1d_fn(x), color="dodgerblue")

#customizing plot -------------------------------S
plt.suptitle('I-V Plot of R Cell', fontsize=20, fontfamily='fantasy')
plt.ylabel('Voltage (mV)', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel('Current (nA)', fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='o', color='paleturquoise', label='I-V Curve',
                          markerfacecolor='paleturquoise', markersize=6),
                   Line2D([0], [0], color='dodgerblue', label='Linear Regression',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper left")
#plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.spring(np.linspace(0, 1, 6)))) #set order of color cycle

#add annotations (arrows and comments) to the plot
#plt.annotate("Slope: 21.83",
#    xy=(260, 743), xycoords='data',
#    xytext=(20, 33), textcoords='offset points',
#    horizontalalignment='right', verticalalignment='bottom')

#plt.annotate('B',
#    xy=(153, 1050), xycoords='data',
#    xytext=(40, -10), textcoords='offset points',
#    arrowprops=dict(facecolor='black', shrink=0.02),
#    horizontalalignment='right', verticalalignment='bottom')

 
# display plot
plt.show()
