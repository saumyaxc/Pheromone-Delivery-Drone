import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math, sys

from randomsearch import randomSearch as rs
from nearestNeighbor import NearestNeighborDistance as nn
# from augmented import augmentedNearestNeighbor as ann

def main():
    
    coordinates = []
    
    while True:
        filename = input("Enter the name of the file: ")
        filepath = f"../data/{filename}"

        try:
            with open(filepath, "r") as file:
                for line in file:
                    x, y = map(float, line.split())
                    coordinates.append((x, y)) 
            break
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.\n")

    print("\nThere are", len(coordinates), "nodes.")

    if len(coordinates) > 256:
        print("The number of nodes exceeds 256! Try again with fewer nodes.")
        sys.exit()

    alg_type = input("\nChoose an algorithm to solve the Pheromone Delivery Drone problem.\n1. Random Search\n2. Nearest Neighbor\n3. Augmented Nearest Neighbor\n\nEnter choice: ")

    while alg_type not in ('1', '2', '3'):
        print("Invalid input. Please enter '1', '2', or '3'.")
        alg_type = input("1. Random Search\n2. Nearest Neighbor\n3. Augmented Nearest Neighbor\n")

    if alg_type == '1':
        print("Running Random Search Algorithm...")
        distance, route = rs(coordinates)

    elif alg_type == '2':
        print("Running Nearest Neighbor Algorithm...")
        distance, route = nn(coordinates)
        
    else:
        print("Running Augmented Nearest Neighbor Algorithm...")
        # ann()
    
    outputfile = filename + "_SOLUTION_" + str(round(distance)) + ".txt"


    # INCLUDE THIS CODE TO CREATE NEW SOLUTION FILE
    # =============================================
    # with open(outputfile, 'w') as f:
    #    for node in route:
    #        f.write(str(node) + ' ')
    # =============================================

    print("==> Route written to disk as", outputfile)
    print("\n")

if __name__ == "__main__":
    main()