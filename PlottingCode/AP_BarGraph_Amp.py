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
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Leech\PeakAmplitude_AllCellsAllTraces.csv")

# make dataframes from data
df = pd.DataFrame(data, columns=["R1_Ctl", "R2_Ctl", "R3_Ctl", "R1_WashIn", "R2_WashIn", "R3_WashIn"])

#calculating values ------------------------------
x1 = np.array(df['R1_Ctl'])
x2 = np.array(df['R2_Ctl'])
x3 = np.array(df['R3_Ctl'])
x4 = np.array(df['R1_WashIn'])
x5 = np.array(df['R2_WashIn'])
x6 = np.array(df['R3_WashIn'])
x1 = x1[~np.isnan(x1)]
x2 = x2[~np.isnan(x2)]
x3 = x3[~np.isnan(x3)]
x4 = x4[~np.isnan(x4)]
x5 = x5[~np.isnan(x5)]
x6 = x6[~np.isnan(x6)]

#averages with built-in numpy function
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
x3_mean = np.mean(x3)
x4_mean = np.mean(x4)
x5_mean = np.mean(x5)
x6_mean = np.mean(x6)
ctl_mean = [x1_mean, x2_mean, x3_mean]
wi_mean = [x4_mean, x5_mean, x6_mean]

#calculating std dev with built-in numpy function
x1_std = np.std(x1)
x2_std = np.std(x2)
x3_std = np.std(x3)
x4_std = np.std(x4)
x5_std = np.std(x5)
x6_std = np.std(x6)
error = [x1_std, x2_std, x3_std]
error2 = [x4_std, x5_std, x6_std]

#multiple bar grouping
x = np.arange(3)
width = 0.35 #width of bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ctl_mean, width, yerr=error, color="dodgerblue", ecolor='black', capsize=7)
rects2 = ax.bar(x + width/2, wi_mean, width, yerr=error2, color="orangered", ecolor='black', capsize=7)

#customizing plot -------------------------------S
# Add some text for labels, title and custom x-axis tick labels, etc.
labels = ['R1', 'R2', 'R3']
ax.set_ylabel('Voltage (mV)', fontsize=14, fontfamily='sans-serif', weight="bold")
ax.set_xlabel('Cell', fontsize=14, fontfamily='sans-serif', weight="bold")
ax.set_title('Averaged Peak Amplitude of R Cells: Control vs. TEA Wash-In', fontsize=20, fontfamily='fantasy')
ax.set_xticks(x, labels, fontsize=14, fontfamily='sans-serif')
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='Control',
                          markerfacecolor='dodgerblue', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='TEA Wash-in',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper right")
 
# display plot
plt.show()
