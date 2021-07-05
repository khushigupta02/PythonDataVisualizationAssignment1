import numpy as np
import pandas as pd 
import seaborn as sns

import matplotlib.pyplot as mpl
import matplotlib.pyplot as plt
%matplotlib inline
x = np.arange(0,9)
y = x*x
print(x)
print(y)

#Line Plot
plt.title("Line Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y)

#####
plt.plot(x,y, 'go--', linewidth=1, markersize=12 )


#Sine WaveForm

plt.title("Sine Waveform")
plt.xlabel("x axis")
plt.ylabel("y axis")
x = np.arange(0,9)
y = x*x

y = np.sin(x)
plt.plot(x,y, color='r')
plt.show()