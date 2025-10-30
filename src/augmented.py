import numpy as np
import math
import time

from nearestNeighbor import NearestNeighborDistance as nn

def euclideanDistance(x, y):
    total = 0
    for i in range(len(x)):
        total += ((x[i] - y[i]) ** 2)
    return math.sqrt(total)

def tour_distance(points, route):
    totalDistance = 0.0
    for i in range(len(route) - 1):
        a, b = route[i], route[i + 1]
        totalDistance += euclideanDistance(points[a], points[b])
    return totalDistance

    def augmentedNearestNeighbor(points):


    print("\nBest Distance:", round(totalDistance, 2), "meters")
    print("Best Route:", route)
    print("Runtime:", round(endTimer - startTimer, 4), "seconds\n")