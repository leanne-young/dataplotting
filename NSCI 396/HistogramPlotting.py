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
#data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-WT-C61DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Lab_2022\DLC\Trial9_DCohort-LY-2022-03-27\results\2022-03-17_F2-KO-C70DLC_resnet50_Trial9_DCohortMar27shuffle1_250000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Lab_2022\DLC\results\2020-11-29_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
#data = pd.read_csv (r"C:\Users\Leanne\Desktop\School\Lab_2022\DLC\results\2020-11-30_F2-KODLC_resnet50_Trial8_DLCMar27shuffle1_200000_filtered.csv")
 
# make dataframe from data
df = pd.DataFrame(data, columns=["Frame", "X_RH", "Y_RH", "Likelihood_RH", "X_LH", "Y_LH", "Likelihood_LH", "X_Pellet", "Y_Pellet", "Likelihood_Pellet"])

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

#calculating values ------------------------------
x = list(range(firstframe+1, lastframe))
#x = df['Frame'].values.tolist()
X_RH = df_RH_filtered['X_RH'].values.tolist()
Y_RH = df_RH_filtered['Y_RH'].values.tolist()
X_LH = df_LH_filtered['X_LH'].values.tolist()
Y_LH = df_LH_filtered['Y_LH'].values.tolist()
X_Pel = df_Pel_filtered['X_Pellet'].values.tolist()
Y_Pel = df_Pel_filtered['Y_Pellet'].values.tolist()

delta_X_RH = []
delta_X_LH = []
delta_X_Pel = []
delta_Y_RH = []
delta_Y_LH = []
delta_Y_Pel = []

delta = 0
for i in range(0,len(x)-1):
    delta_X_RH.append(abs(X_RH[i] - X_RH[i+1]))
    delta_Y_RH.append(abs(Y_RH[i] - Y_RH[i+1]))
    delta_X_LH.append(abs(X_LH[i] - X_LH[i+1]))
    delta_Y_LH.append(abs(Y_LH[i] - Y_LH[i+1]))
    delta_X_Pel.append(abs(X_Pel[i] - X_Pel[i+1]))
    delta_Y_Pel.append(abs(Y_Pel[i] - Y_Pel[i+1]))

RH_binCount = len(delta_X_RH)
LH_binCount = len(delta_X_LH)
Pel_binCount = len(delta_X_Pel)

#Hist plots -------------------
#plotting each line separately to manually change colors and properties easily
plt.hist(delta_X_RH, color="blueviolet", histtype="step", bins=RH_binCount, alpha=1, linewidth=1.3)
plt.hist(delta_X_LH, color="springgreen", histtype="step", bins=LH_binCount, alpha=1, linewidth=1.3)
plt.hist(delta_X_Pel, color="orangered", histtype="step", bins=Pel_binCount, alpha=1, linewidth=1.3)
plt.hist(delta_Y_RH, color="blueviolet", histtype="step", bins=RH_binCount, alpha=1, linewidth=1.3)
plt.hist(delta_Y_LH, color="springgreen", histtype="step", bins=LH_binCount, alpha=1, linewidth=1.3)
plt.hist(delta_Y_Pel, color="orangered", histtype="step", bins=Pel_binCount, alpha=1, linewidth=1.3)

#customizing plot
plt.suptitle(r"$\Delta$ X and $\Delta$ Y of Tracked Coordinates", fontsize=25, fontfamily='fantasy')
plt.ylabel('Frequency', fontsize=14, fontfamily='sans-serif', weight="bold") #add and customize y axis label
plt.xlabel(r"$\Delta$ X and $\Delta$ Y", fontsize=14, fontfamily='sans-serif', weight="bold") #customize x axis label

#video1
#plt.xlim(11, 1200) #(15, 1200) #11,1230)
#plt.ylim(0, 12.5) #0, 12.3)#7.1)

#video2
plt.xlim(11, 1200) #(15,1200) #(11,1230)
plt.ylim(0,12.5) #(0,12.3)

#video3
#plt.xlim (11, 650) #(5, 650)# #10,700)
#plt.ylim(0,11.5)

#video4
#plt.xlim(11, 650) #(5,650)
#plt.ylim(0,11.5)

#legend
#line 2D uses a line marker object of our choice for the legend, here I used a square marker
legend_elements = [Line2D([0], [0], marker='s', color='w', label='Right Paw',
                          markerfacecolor='blueviolet', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Left Paw',
                          markerfacecolor='springgreen', markersize=10),
                    Line2D([0], [0], marker='s', color='w', label='Pellet',
                          markerfacecolor='orangered', markersize=10)]

plt.legend(handles=legend_elements, loc="upper right")
fig = plt.gcf()
fig.set_size_inches(13,5)

# display plot
plt.show()
