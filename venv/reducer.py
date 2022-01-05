# Daimeun Praytor

import csv

f = open("dictLabel.txt", "r")
f2 = open("dictXY.txt", "r")
lines = f.readlines()
line2 = f2.readline()

# Gets the number of data points
numDataPoints = int(line2)

# Gets the X and Y values for the plotter
lines2 = f2.read().splitlines()

xValues = []
for number in lines2:
    xValues.append(float(number.split('\t')[0]))

yValues = []
for number in lines2:
    yValues.append(float(number.split('\t')[1]))
f2.close()

# Creates a dictionary for all of the results
resultDict = {}
for datapoint in range(numDataPoints):
    currentX = xValues[datapoint]
    currentY = yValues[datapoint]

    key = (currentX, currentY)

    # Creates a list and stores each columns result in a value list, these are the labels for that data point
    value = []
    for x in lines:
        value.append(x.split('\t')[datapoint])

    resultDict.update({key: value})
f.close()

# Creates list to store the most frequent labels for each data point.
labelList = []
for datapoint in resultDict:
    currentList = resultDict[datapoint]
    counter = 0
    number = currentList[0]

    for i in currentList:
        numberFreq = currentList.count(i)
        if numberFreq > counter:
            counter = numberFreq
            number = i
    labelList.append(int(number))




