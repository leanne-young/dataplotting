#Compare average aspect ratio values

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np

#import csv's
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Maggots\FedLarva.csv")
data2 = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Maggots\StarvedLarva.csv")

# make dataframes from data
df = pd.DataFrame(data, columns=["AR"])
df2 = pd.DataFrame(data2, columns=["AR"])

#calculating values ------------------------------
x1 = np.array(df['AR'])
x2 = np.array(df2['AR'])

#averages with built-in numpy function
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
toPlot = [x1_mean, x2_mean]
print(toPlot)

#calculating std dev with built-in numpy function
x1_std = np.std(x1)
x2_std = np.std(x2)
error = [x1_std, x2_std]

x = np.arange(2)
fig, ax = plt.subplots()
ax.bar(x, toPlot, color="blue", yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_xticks(x)

#customizing plot -------------------------------S
# Add some text for labels, title and custom x-axis tick labels, etc.
labels = ['Fed', 'Starved']
ax.set_ylabel('Average Aspect Ratio', fontsize=14, fontfamily='sans-serif', weight="bold")
#ax.set_xlabel('Cell', fontsize=14, fontfamily='sans-serif', weight="bold")
ax.set_title('Average Aspect Ratio of Fed vs. Starved Larvae', fontsize=25, fontfamily='fantasy')
ax.set_xticks(x, labels, fontsize=14, fontfamily='sans-serif', weight="bold")
#ax.legend()

barlist = plt.bar(x, toPlot)
barlist[0].set_color('dodgerblue')
barlist[1].set_color('orangered')

fig.tight_layout()
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
#legend_elements = [Line2D([0], [0], marker='s', color='w', label='Control',
#                          markerfacecolor='dodgerblue', markersize=10),
#                    Line2D([0], [0], marker='s', color='w', label='TEA Wash-in',
#                          markerfacecolor='orangered', markersize=10)]
#plt.legend(handles=legend_elements, loc="upper right")
 
# display plot
plt.show()