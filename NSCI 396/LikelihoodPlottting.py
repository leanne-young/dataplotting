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

#import csv
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-WT-C61DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-KO-C70DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\results\2020-11-29_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Iron Precision\Desktop\School\Lab_2022\DLC\results\2020-11-30_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
 
# make dataframe from data
df = pd.DataFrame(data, columns=["Frame", "Likelihood_RH", "Likelihood_LH","Likelihood_Pellet"])

#frame bounds
#dim working---------------
#firstframe = 8280;
#lastframe = 8580;
#dim not working--------------
firstframe = 8250;
lastframe = 8550;
#Camilla working---------------
#firstframe = 3210;
#lastframe = 3420;
#camilla not working---------------
#firstframe = 11190;
#lastframe = 11490;

df_RH_filtered = df[df['Frame'] > firstframe]
df_RH_filtered = df_RH_filtered[df_RH_filtered['Frame'] < lastframe]
df_LH_filtered = df[df['Frame'] > firstframe]
df_LH_filtered = df_LH_filtered[df_LH_filtered['Frame'] < lastframe]
df_Pel_filtered = df[df['Frame'] > firstframe]
df_Pel_filtered = df_Pel_filtered[df_Pel_filtered['Frame'] < lastframe]

#plotting subsets ------------------------------
#plotting each line separately to manually change colors and properties easily
x = list(range(firstframe+1, lastframe))
y1 = df_RH_filtered['Likelihood_RH']
y2 = df_LH_filtered['Likelihood_LH']
y3 = df_Pel_filtered['Likelihood_Pellet']


#Line plots -------------------
#Righthand
plt.plot(x,y1, color="blueviolet", alpha=0.75)
#Lefthand
plt.plot(x,y2, color="springgreen", alpha=0.75)
#Pellet
plt.plot(x,y3, color="orangered", alpha=0.75)

#customizing plot
plt.suptitle('Likelihood of DLC Tracking Predictions', fontsize=25, fontfamily='fantasy')
plt.ylabel('Likelihood', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel('Frame', fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label
#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='Right Paw',
                          markerfacecolor='blueviolet', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Left Paw',
                          markerfacecolor='springgreen', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Pellet',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper right", bbox_to_anchor=(1.12, 1), borderaxespad=0) #bbox_to_anchor=(1.15, 1)
fig = plt.gcf()
fig.set_size_inches(14,5)

# display plot
plt.show()



