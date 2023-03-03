import numpy as np
import matplotlib.pyplot as plt

# Sensor data
acceleration_data = np.loadtxt("./Data/Accelerometer.csv", dtype=float, delimiter=",", skiprows=1)
gyroscope_data = np.loadtxt("./Data/Gyroscope.csv", dtype=float, delimiter=",", skiprows=1)
location_data = np.loadtxt("./Data/Location.csv", dtype=float, delimiter=",", skiprows=1)

# NOTE: Usefull data in acceleration_data is 2nd column, and in gyroscope_data is 3rd column

# Variables for processing
pos = np.zeros((len(acceleration_data), 2))
velocity = np.zeros((len(acceleration_data), 2))
angle = np.zeros(len(acceleration_data))

for t in range(1, len(acceleration_data)):
    dt = acceleration_data[t, 0] - acceleration_data[t - 1, 0]
    angle[t] = angle[t - 1] + gyroscope_data[t - 1, 3] * dt

plt.plot(gyroscope_data[:, 0], gyroscope_data[:, 3])
plt.plot(gyroscope_data[:, 0], np.degrees(angle))

# Plotting
# fig, axs = plt.subplots(2)
# axs[0].set_title("Acceleration: Planar")
# axs[0].plot(acceleration_data[:, 0], acceleration_data[:, 2])
# axs[1].set_title("Velocity: Gyroscopic")
# axs[1].plot(gyroscope_data[:, 0], gyroscope_data[:, 3])

# for ax in axs.flat:
#     ax.set(xlabel='Time: s')

# axs[0].set(ylabel="Acceleration: $m/s^2$")
# axs[1].set(ylabel="Velocity: $rad/s$")

# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

plt.show()