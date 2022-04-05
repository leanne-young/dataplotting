# Code to plot data for my research and lab courses

## Leech Research Project

### AP_OverlayPlot.py
Overlays the action potentials of 3 different cells before and after TEA drug wash-in. The action potentials are derived from the average trace, calculated from Clampfit.

### AP_PhasePlot.py
Overlays the phase plots of the action potentials of 3 different cells before and after TEA drug wash-in. The same averaged data used in AP_Overlay.py is used to calculate dV/dt that is plotted here.

### AP_BarGraph_Amp.py
Plots the average amplitude of the action potentials of each cell. Data is derived from the amplitude measurement feature on Clampfit, which outputs the peak amplitude of each AP event in all the traces of each recording. All calculations are made with Numpy built-in functions.

### AP_BarGraph_Dur.py
Plots the average duration of the action potentials of each cell, data derived from the average trace.

### plotting.py
[older version code] Plotting the recordings from our Leech module data collection.
Overlays 2 different action potentials to compare their differences.
