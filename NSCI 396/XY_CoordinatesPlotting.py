#Plot DLC results

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.pyplot import figure
import numpy as np
from scipy.interpolate import interp1d

#import csv
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-WT-C61DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-KO-C70DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\results\2020-11-29_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\results\2020-11-30_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
 
# make dataframe from data
df = pd.DataFrame(data, columns=["Frame", "X_RH", "Y_RH", "Likelihood_RH", "X_LH", "Y_LH", "Likelihood_LH", "X_Pellet", "Y_Pellet", "Likelihood_Pellet"])
#only keep rows with a likelihood higher than the p_cutoff we set
#p_cutoff = 0.8

#frame bounds
#dim working---------------
#firstframe = 8280;
#lastframe = 8580;
#dim not working--------------
#firstframe = 8250;
#lastframe = 8550;
#Camilla working---------------
#firstframe = 3210;
#lastframe = 3420;
#camilla not working---------------
firstframe = 11190;
lastframe = 11490;

df_RH_filtered = df[df['Likelihood_RH'] > 0.8]
df_LH_filtered = df[df['Likelihood_LH'] > 0.8]
df_Pel_filtered = df[df['Likelihood_Pellet'] > 0.8]

df_RH_filtered = df_RH_filtered[df_RH_filtered['Frame'] > firstframe]
df_RH_filtered = df_RH_filtered[df_RH_filtered['Frame'] < lastframe]
df_LH_filtered = df_LH_filtered[df_LH_filtered['Frame'] > firstframe]
df_LH_filtered = df_LH_filtered[df_LH_filtered['Frame'] < lastframe]
df_Pel_filtered = df_Pel_filtered[df_Pel_filtered['Frame'] > firstframe]
df_Pel_filtered = df_Pel_filtered[df_Pel_filtered['Frame'] < lastframe]

# plot multiple columns such as population and year from dataframe ---------------------
#df_Pel_filtered.plot(x="Frame", y=["X_RH", "Y_RH", "X_LH", "Y_LH", "X_Pellet", "Y_Pellet"], kind="line", figsize=(5000, 6))
#df_Pel_filtered.plot(x="Frame", y=["X_Pellet", "Y_Pellet"], kind="line", figsize=(5000, 6))
#df_Pel_filtered.plot(x="Frame", y=["X_RH", "Y_RH", "X_LH", "Y_LH"], kind="line", figsize=(5000, 6))

#plotting subsets ------------------------------
#plotting each line separately to manually change colors and properties easily
#df_subset.plot(x="Frame", y=["X_RH", "Y_RH", "X_LH", "Y_LH", "X_Pellet", "Y_Pellet"], kind="line", figsize=(4000, 6))
x = list(range(firstframe+1, lastframe))
x1 = df_RH_filtered['Frame']
x2 = df_LH_filtered['Frame']
x3 = df_Pel_filtered['Frame']
y1 = df_RH_filtered['X_RH']
y2 = df_RH_filtered['Y_RH']
y3 = df_LH_filtered['X_LH']
y4 = df_LH_filtered['Y_LH']
y5 = df_Pel_filtered['X_Pellet']
y6 = df_Pel_filtered['Y_Pellet']

#Line plots -------------------
#Righthand
#plt.plot(x1,y1, color="blueviolet", label="Right Paw")
#plt.plot(x1,y2, color="blueviolet", linestyle='dotted')
#Lefthand
#plt.plot(x2,y3, color="springgreen", label="Left Paw")
#plt.plot(x2,y4, color="springgreen", linestyle='dotted')
#Pellet
#plt.plot(x3,y5, color="orangered", label="Pellet")
#plt.plot(x3,y6, color="orangered", linestyle='dotted')

# --------- Scatterplots ----------------
#Righthand---------------
plt.scatter(x1,y1, color="blueviolet", s=10, alpha=1)
plt.scatter(x1,y2, color="blueviolet", s=10, alpha=1, facecolors='none', marker='d')
#plt.scatter(x1,y2, color="rebeccapurple", s=5)
#Lefthand---------------
plt.scatter(x2,y3, color="springgreen", s=10, alpha=1)
plt.scatter(x2,y4, color="springgreen", s=10, alpha=1, facecolors='none', marker='d')
#plt.scatter(x2,y4, color="mediumseagreen", s=5, alpha=0.75)
#Pellet--------------
plt.scatter(x3,y5, color="orangered", s=10, alpha=1)
plt.scatter(x3,y6, color="orangered", s=10, alpha=1, facecolors='none', marker='d')
#plt.scatter(x3,y6, color="salmon", s=5, alpha=0.75)

# cubic (spline) ---------------
#f = interp1d(x, y1)
#f2 = interp1d(x, y2)
#f3 = interp1d(x, y3, kind='cubic')
#f4 = interp1d(x, y4, kind='cubic')
#f5 = interp1d(x, y5, kind='cubic')
#f6 = interp1d(x, y6, kind='cubic')
###plt.plot(x, f(x), color="blueviolet")
###plt.plot(x,f2(x), color="blueviolet", linestyle='dotted')
###plt.plot(x,f3(x), color="springgreen")
###plt.plot(x,f4(x), color="springgreen", linestyle='dotted')
###plt.plot(x,f5(x), color="orangered")
###plt.plot(x,f6(x), color="orangered", linestyle='dotted')


#customizing plot
plt.suptitle('Tracked XY Coordinates of Paws & Pellet', fontsize=25, fontfamily='fantasy', y=.95)
plt.ylabel('Position (in pixels)', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel('Frame', fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='Right Paw',
                          markerfacecolor='blueviolet', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Left Paw',
                          markerfacecolor='springgreen', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Pellet',
                          markerfacecolor='orangered', markersize=10),
                    Line2D([0], [0], marker='o', color='w', markersize='7', 
                          markerfacecolor='gray', label="X"),
                    Line2D([0], [0], marker='d', color='w', markersize='7', 
                          markerfacecolor='none', markeredgecolor='gray', label="Y")]
                    #Line2D([0], [0], color='gray', lw=1.5, label='X'),
                    #Line2D([0], [0], color='gray', lw=1.5, linestyle="dotted", label='Y')]

plt.legend(handles=legend_elements, loc="upper right")
#plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.spring(np.linspace(0, 1, 6)))) #set order of color cycle

#set size
fig = plt.gcf()
fig.set_size_inches(14,7)

#add annotations (arrows and comments) to the plot
#Pellet incorrectly identified at corner of cage
#plt.annotate('A',
#    xy=(260, 743), xycoords='data',
#    xytext=(20, 33), textcoords='offset points',
#    arrowprops=dict(facecolor='black', shrink=0.02),
#    horizontalalignment='right', verticalalignment='bottom')

#Pellet correctly identified in front of slit
#plt.annotate('B',
#    xy=(153, 1050), xycoords='data',
#    xytext=(40, -10), textcoords='offset points',
#    arrowprops=dict(facecolor='black', shrink=0.02),
#    horizontalalignment='right', verticalalignment='bottom')

 
# display plot
plt.show()