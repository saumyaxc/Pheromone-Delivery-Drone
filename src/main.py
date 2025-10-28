import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from randomsearch import randomSearch as rs
# from nearestneighbor import nearestNeighbor as nn
# from augmented import augmentedNearestNeighbor as ann

def main():
    coordinates = []
    filename = input("Enter filename: ")
    filepath = f"../data/{filename}"

    with open(filepath, "r") as file:
        for line in file:
            x, y = map(float, line.split())
            coordinates.append((x, y))
    
    
    alg_type = input("Choose an algorithm to solve the Pheromone Delivery Drone problem.\n1. Random Search\n2. Nearest Neighbor\n3. Augmented Nearest Neighbor\nEnter choice: ")

    while alg_type not in ('1', '2', '3'):
        print("Invalid input. Please enter '1', '2', or '3'.")
        alg_type = input("1. Random Search\n2. Nearest Neighbor\n3. Augmented Nearest Neighbor\n")

    if alg_type == '1':
        print("Running Random Search Algorithm...")
        rs(coordinates)

    elif alg_type == '2':
        print("Running Nearest Neighbor Algorithm...")
        # nn()
    else:
        print("Running Augmented Nearest Neighbor Algorithm...")
        # ann()

    

if __name__ == "__main__":
    main()