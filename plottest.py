import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 200, -100*110, 100*110])

for i in range(0,200):
    if i<100:
        y = i**2
    else:
        y = 100*100
    plt.scatter(i, y, c='blue', linewidths=0.001, label='k1')
    plt.scatter(i, -y, c='red', linewidths=0.001, label='k2')
    plt.pause(0.02)

plt.show()