import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here



# This will draw the graph
plt.plot( xdata, ydata, 'bo')
xxx = np.linspace(0,1,100)
yyy = xxx*xxx + 0.5
yyy2 = xxx*xxx - 0.5
plt.plot( xxx, yyy, 'k-' )
plt.plot( xxx, yyy2, 'k-' )
plt.savefig("correlated_variables.png")
