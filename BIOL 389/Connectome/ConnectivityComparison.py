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
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Mel_vs_San.csv")

# make dataframes from data
df = pd.DataFrame(data, columns=["Mel_Synapses", "Mel_Neurons", "San_Synapses", "San_Neurons"])

#getting values ------------------------------
x1 = np.array(df['Mel_Synapses'])
x2 = np.array(df['Mel_Neurons'])
x3 = np.array(df['San_Synapses'])
x4 = np.array(df['San_Neurons'])

melano = [int(x1), int(x2)]
santo = [int(x3), int(x4)]

#multiple bar grouping
x = np.arange(2)
width = 0.35 #width of bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, melano, width, color="dodgerblue")
rects2 = ax.bar(x + width/2, santo, width, color="orangered")

#customizing plot -------------------------------S
# Add some text for labels, title and custom x-axis tick labels, etc.
labels = ['Synapses', 'Neurons']
ax.set_ylabel('Count', fontsize=14, fontfamily='sans-serif', weight="bold")
ax.set_title('Connectivity Comparison', fontsize=25, fontfamily='fantasy')
ax.set_xticks(x, labels, fontsize=14, fontfamily='sans-serif', weight="bold")
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='$\it{D. melanogaster}$',
                          markerfacecolor='dodgerblue', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='$\it{D. santomea}$',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper right")
 
# display plot
plt.show()