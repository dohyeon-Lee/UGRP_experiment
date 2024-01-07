import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "~/ros2_ws/src/reading_sensor/measured/experiment.csv"

data = pd.read_csv(file_path)

plt.figure(figsize=(20, 20))
i=0
for column in data.columns:
    i += 1
    plt.subplot(1,1,i)
    time = np.linspace(0, len(data[column].tolist())/50, len(data[column].tolist()))
    plt.plot(time, data[column].tolist(), label=column)
    plt.title(column)
plt.show()