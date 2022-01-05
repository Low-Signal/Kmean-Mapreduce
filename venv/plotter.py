# Daimeun Praytor

import reducer as reducer
import matplotlib.pyplot as plt
import numpy as np

# Plots the reduced data points
colormap = np.array(['red', 'blue', 'yellow', 'black', 'cyan', 'magenta', 'gray', 'darkgreen', 'lime', 'orangered'])
plt.title('K Means Classification Map - Digits Data Set - Reduced')
plt.scatter(reducer.xValues, reducer.yValues, c=colormap[reducer.labelList], s=40)
plt.show()