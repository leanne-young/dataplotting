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
R1_Ctl_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R1_Ctl.csv")
R2_Ctl_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R2_Ctl.csv")
R3_Ctl_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R3_Ctl.csv")
R1_WashIn_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R1_WashIn.csv")
R2_WashIn_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R2_WashIn.csv")
R3_WashIn_data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\R3_WashIn.csv")

# make dataframes from data
R1_Ctl_df = pd.DataFrame(R1_Ctl_data, columns=["Time", "V"])
R2_Ctl_df = pd.DataFrame(R2_Ctl_data, columns=["Time", "V"])
R3_Ctl_df = pd.DataFrame(R3_Ctl_data, columns=["Time", "V"])
R1_WashIn_df = pd.DataFrame(R1_WashIn_data, columns=["Time", "V"])
R2_WashIn_df = pd.DataFrame(R2_WashIn_data, columns=["Time", "V"])
R3_WashIn_df = pd.DataFrame(R3_WashIn_data, columns=["Time", "V"])

#plotting subsets ------------------------------
#plotting each line separately to manually change colors and properties easily
#R1_Ctl
x1 = R1_Ctl_df['Time']
y1 = R1_Ctl_df['V']
#R2_Ctl
x2 = R2_Ctl_df['Time']
y2 = R2_Ctl_df['V']
#R3_Ctl
x3 = R3_Ctl_df['Time']
y3 = R3_Ctl_df['V']
#R1_WashIn
x4 = R1_WashIn_df['Time']
y4 = R1_WashIn_df['V']
#R2_WashIn
x5 = R2_WashIn_df['Time']
y5 = R2_WashIn_df['V']
#R3_WashIn
x6 = R3_WashIn_df['Time']
y6 = R3_WashIn_df['V']

#Line plots ------------------------------

plt.figure()
colors = plt.cm.Blues(np.linspace(0,1,4))
plt.plot(x1, y1, color="paleturquoise")#color=colors[0])
plt.plot(x2, y2, color="deepskyblue")#color=colors[1])
plt.plot(x3, y3, color="dodgerblue")#color=colors[2])
plt.plot(x4, y4, color="mistyrose")#color=colors[0])
plt.plot(x5, y5, color="coral")#color=colors[1])
plt.plot(x6, y6, color="orangered")#color=colors[2])

#customizing plot -------------------------------S
plt.suptitle('Averaged AP of R Cells: Control vs. TEA Wash-In', fontsize=20, fontfamily='fantasy')
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
