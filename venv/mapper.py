# Daimeun Praytor

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import sklearn.metrics as sm

import pandas as pd
import numpy as np


digits = datasets.load_digits()

# Principal Component Analysis to reduce from 64 to 2 features.
pca = PCA(n_components=2)
pca.fit(digits.data)
transformedData = pca.transform(digits.data)

x = pd.DataFrame(transformedData)

x.columns = ['One', 'Two']

# Builds machine learning model and runs the Kmeans algorithm on the dataset.
model = KMeans(n_clusters=10)
model.fit(x)

# Stores the labels for the current mapper
f = open("dictLabel.txt", "a")

# Stores the number of data points, and the X and Y data
f2 = open("dictXY.txt", "w")
f2.write(str(digits.data.shape[0]))
f2.write("\n")

# Creates a dictionary to store each  'x' 'y' and their corresponding label
dataDict = {}
dataValues = x.values
for datapoint in range(digits.data.shape[0]):
    # Converts the numpy array into a tuple to be passed into the dictionary key
    f2.write(str(round(dataValues[datapoint, 0], 5)))
    f2.write("\t")
    f2.write(str(round(dataValues[datapoint, 1], 5)))
    f2.write("\n")

    # Sets the key:value pairs
    key = (round(dataValues[datapoint, 0], 5), round(dataValues[datapoint, 1], 5))
    value = model.labels_[datapoint]

    f.write(str(value))
    f.write('\t')

    dataDict.update({key: value})

f.write('\n')

f.close()
f2.close()
