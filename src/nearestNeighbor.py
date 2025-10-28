import numpy as np
import math

#basic KNN algorithm - used geeksforgeeks for algorithm reference
def euclideanDistance(x, y):
    total = 0
    for i in range(len(x)):
        total += ((x[i]-y[i])**2)
    return math.sqrt(total)

def NearestNeighborDistance (trainingData, testVal, k):
    distance = []
    for i in range(len(trainingData)):
        dist = euclideanDistance(testVal, trainingData[i])
        distance.append([dist, trainingData[i]])

    #sort by distance:
    for i in range(len(distance)):
        for j in range (i+1, len(distance)):
            if distance[i][0] > distance[j][0]:
                temp = distance[i]
                distance[i] = distance[j]
                distance[j] = temp
    
    nearestAlg = []
    for i in range(k):
        nearestAlg.append(distance[i])
    
    return nearestAlg

#TEMP TEST CASE - sample
trainingData = [[1,1], [1,2], [2,3], [2,2], [3,4], [5,6],[7,8]]

testVal = [3,3]
k = 1

nearestVals = NearestNeighborDistance(trainingData, testVal, k)

for i, j in nearestVals:
    print("Point:", j, "Distance:", i)
   
    