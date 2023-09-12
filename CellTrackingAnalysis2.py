import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#user inputs following values:
csv = 'FUCCI cell cycle tracking - FUCCI cell cycle tracking.csv.csv'
start_index = 0 #row index to start plot at
end_index = 60 #row index to end plot at
end_file_name = "intensities.png" #name of png produced

#clean up data, create new DataFrame with only columns of interest
df = pd.read_csv(csv)
df = df.drop([0, 1])
selected_columns = ['TRACK_ID','FRAME', 'POSITION_X', 'POSITION_Y', 'POSITION_T', 'MEAN_INTENSITY_CH1', 'MEAN_INTENSITY_CH2']
new_df = df[selected_columns]
new_df = new_df.astype(float)
new_df = new_df.sort_values(by = ['TRACK_ID','POSITION_T'])
subset_df = new_df.iloc[0:60]


c1_intensity = subset_df['MEAN_INTENSITY_CH1']
c2_intensity = subset_df['MEAN_INTENSITY_CH2']
x = subset_df['POSITION_X']
y = subset_df['POSITION_Y']
t = subset_df['POSITION_T']
frame = subset_df['FRAME']

#compute instantaneous speed between each coordinate pair
dx = np.diff(x)
dy = np.diff(y)
dt = np.diff(t)
speed = np.sqrt((dx/dt)**2 + (dy/dt)**2)
time_midpoints = [0.5 * (t1 + t2) for t1, t2 in zip(t[:-1], t[1:])]

#plot red intensity, green intensity, and instanteous speed
plt.plot(t, c1_intensity, label = 'G1 (red) intensity', color = 'red')
plt.plot(t, c2_intensity, label = 'G2 (green) intensity', color = 'green')
plt.plot(time_midpoints, speed, label = 'Instantaneous speed')
plt.xlabel('Time')
plt.ylabel('Intensities')
plt.legend()

plt.savefig(end_file_name)
