#Plot AP duration

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

#calculating values ------------------------------
#R1_Ctl
x1 = R1_Ctl_df['Time'].iloc[-1]
y1 = np.array(R1_Ctl_df['V'])
#R2_Ctl
x2 = R2_Ctl_df['Time'].iloc[-1]
y2 = np.array(R2_Ctl_df['V'])
#R3_Ctl
x3 = R3_Ctl_df['Time'].iloc[-1]
y3 = np.array(R3_Ctl_df['V'])
#R1_WashIn
x4 = R1_WashIn_df['Time'].iloc[-1]
y4 = np.array(R1_WashIn_df['V'])
#R2_WashIn
x5 = R2_WashIn_df['Time'].iloc[-1]
y5 = np.array(R2_WashIn_df['V'])
#R3_WashIn
x6 = R3_WashIn_df['Time'].iloc[-1]
y6 = np.array(R3_WashIn_df['V'])

#make an array of the avgs
ctl_avg = (x1+x2+x3) / 3 #(11.5+16.8+ 16.6+ 17.5)/4
WI_avg = (x4+x5+x6) / 3 #(17.2+ 53.5+ 63.9+ 55.7)/4
toPlot = [ctl_avg, WI_avg]
ctl = np.array([x1, x2, x3]) #[11.5, 16.8, 16.6, 17.5]
WI = np.array([x4, x5, x6]) #[17.2, 53.5, 63.9, 55.7]
#std dev
Ctl_std = np.std(ctl)
WI_std = np.std(WI)
error = [Ctl_std, WI_std]

x = np.arange(2)
fig, ax = plt.subplots()
ax.bar(x, toPlot, color="blue", yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_xticks(x)

barlist = plt.bar(x, toPlot)
barlist[0].set_color('dodgerblue')
barlist[1].set_color('orangered')

#multiple bar grouping
#x = np.arange(3)
#width = 0.35 #width of bars
#fig, ax = plt.subplots()
#rects1 = ax.bar(x - width/2, ctl, width, color="dodgerblue", label='Control')
#rects2 = ax.bar(x + width/2, WI, width, color="orangered", label='TEA Wash-in')

#customizing plot -------------------------------S
#plt.suptitle('Action Potential of Control vs. TEA Wash-In', fontsize=20, fontfamily='fantasy')
#plt.ylabel('Voltage (mV)', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
#plt.xlabel('Time (ms)', fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label

# Add some text for labels, title and custom x-axis tick labels, etc.
labels = ['Control', 'TEA Wash-In']
ax.set_ylabel('Time (ms)', fontsize=14, fontfamily='sans-serif', weight="bold")
ax.set_title('Averaged AP Duration of R Cells: Control vs. TEA Wash-In', fontsize=20, fontfamily='fantasy')
ax.set_xticks(x, labels, fontsize=14, fontfamily='sans-serif', weight="bold")
#ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
#legend_elements = [Line2D([0], [0], marker='s', color='w', label='Control',
#                          markerfacecolor='dodgerblue', markersize=10),
#                    Line2D([0], [0], marker='s', color='w', label='TEA Wash-in',
#                          markerfacecolor='orangered', markersize=10)]

#plt.legend(handles=legend_elements, loc="upper left")
 
# display plot
plt.show()
