import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 120, -550, 550])
x_old = 0; y_old = 0;

for i in range(0, 120):
    x = i;
    if i<=20:
        y = i**2;
    elif i>20 and i <80:
        y = 400 + 2*(i-20);
    else:
         y = 520
    
    plt.plot([x_old, x], [y_old, y], c='b')
    plt.plot([x_old, x], [-y_old, -y], c='r')
    plt.pause(0.01)
    x_old = x;
    y_old = y;
    
plt.show()