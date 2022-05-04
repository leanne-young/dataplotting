# Code to plot data for my research and lab courses

## 🐭 NSCI 396 Research Project
(Files located in the `NSCI 396` folder)

### BarGraphPlotting.py
Calculates the uR score of 2 different trials being analyzed using the uR score equations defined in my report. Then plots a bar graph comparing the performance of both.

### HistogramPlotting.py
Calculates delta_X and delta_Y values and plots a histogram of the frequencies of consecutive coordinate differences of a trial. Rerun the script for each trial being analyzed to obtain the histogram for it. Histograms are modeled after the DLC output histograms (Mathis et al., 2018).

### LikelihoodPlotting.py
Plots the network confidence likelihood of a trial. You can isolate each element of interest (i.e. each color line representing a paw or pellet) for easier analysis. Modeled after the DLC output likelihood plot (Mathis et al., 2018).

### LossFunctionPlotting.py
Plots the loss function over iterations of network training.

### TrajectoryPlotting.py
Plots a cumulative trajectory plot of a trial. Points are plotted over the whole duration of the video. Modeled after the DLC output trajectory plot (Mathis et al., 2018).

### XY_CoordinatesPlotting.py
Plots the X and Y coordinates separately over time (in frames). Modeled after the DLC output XY coordinates plot (Mathis et al., 2018).

_________________________________________

## 🧠  Connectome Research Project
(Python files and data files located in the `BIOL 389` > `Connectome` folder)

### ConnectivityComparison.py
Plots a bar graph to give a visual comparison between the number of presynaptic connections and upstream neurons in *D. melanogaster* and *D. santomea*.

_________________________________________

## 🔬 Leech Research Project
(Python files located in the `PlottingCode` folder, data files located in the `Data` folder)

### AP_OverlayPlot.py
Overlays the action potentials of 3 different cells before and after TEA drug wash-in. The action potentials are derived from the average trace, calculated from Clampfit.

### AP_PhasePlot.py
Overlays the phase plots of the action potentials of 3 different cells before and after TEA drug wash-in. The same averaged data used in AP_Overlay.py is used to calculate dV/dt that is plotted here.

### AP_BarGraph_Amp.py
Plots the average amplitude of the action potentials of each cell. Data is derived from the amplitude measurement feature on Clampfit, which outputs the peak amplitude of each AP event in all the traces of each recording. All calculations are made with Numpy built-in functions.

### AP_BarGraph_Dur.py
Plots the average duration of the action potentials of each cell, data derived from the average trace.

### IV_LinePlot.py
Creates an I-V Plot of our own recording to analyze the passive membrane properties of our cell.

### plotting.py
[older version code] Plotting the recordings from our Leech module data collection.
Overlays 2 different action potentials to compare their differences.

_________________________________________

## 🪰  Drosophila Larvae Research Project
(Python files and data files located in the `BIOL 389` > `Maggot` folder)

### obstacle_ppk.py
Controls the red LED light to optogenetically activate nociceptors to simulate a painful obstacle in the middle of the agar plate.

### opto_autopy_masked_ppk_obstacle.bonsai
Bonsai workflow to record trials, calculate XY coordinates of the larvae centroid, and facilitate control of the LED with `obstacle_ppk.py` by communicating with the Arduino microcontroller.

### AspectRatio_AnglePlot.py
Plots the aspect ratio of the ellipse (larva) by time to quantify body reorientations. Variables can be changed to plot the adjusted angles of the ellipse by time, which shows body orientation.

### AR_Comparison.py
Compares the average aspect ratio of the fed larva and of the starved larva as a bar graph.
