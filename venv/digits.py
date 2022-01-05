# Daimeun Praytor

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import sklearn.metrics as sm

import pandas as pd
import numpy as np

digits = datasets.load_digits()

x = pd.DataFrame(digits.data)

# Converts 64 components to 2
pca = PCA(n_components=2)
pca.fit(digits.data)
transformedData = pca.transform(digits.data)

x = pd.DataFrame(transformedData)

x.columns = ['One', 'Two']

# Preforms k means algorithm on the dataset
model = KMeans(n_clusters=10)
model.fit(x)

colormap = np.array(['red', 'blue', 'yellow', 'black', 'cyan', 'magenta', 'gray', 'darkgreen', 'lime', 'orangered'])

# Plot the Models Classifications
plt.scatter(x.One, x.Two, c=colormap[model.labels_], s=40)
plt.title('K Means Classification - Digits Data Set - No Reducer')

plt.show()