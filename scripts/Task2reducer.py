#!/usr/bin/env python3
import sys
import math

def euclidean_distance(x1, y1, x2, y2):
    # Calculating the Euclidean distance between two points (x1, y1) and (x2, y2)
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

current_medoid = None  # Variable to keep track of the current medoid being processed
cluster_points = []  # List to store points in the current cluster

# Reading the input data from stdin, where each line contains a medoid and associated trip data
for line in sys.stdin:
    # Spliting the input line into medoid and trip data
    medoid, trip_data = line.strip().split("\t")
    trip_id, dropoff_x, dropoff_y = trip_data.split(',')
    
    # Converting medoid string to a tuple of floats (x, y)
    medoid_tuple = tuple(map(float, medoid.strip('()').split(',')))
    
    # If the medoid changes, process the current cluster to find the best medoid
    if current_medoid != medoid_tuple:
        if current_medoid is not None:
            # Initialize the best medoid as the current one and the minimum cost as infinity
            best_medoid = current_medoid
            min_cost = float('inf')
            
            # Iterate over all points in the current cluster and calculate the total cost (sum of distances)
            for i, (tx, ty) in enumerate(cluster_points):
                cost = sum(euclidean_distance(tx, ty, x, y) for (x, y) in cluster_points)
                # Update the best medoid if a lower cost is found
                if cost < min_cost:
                    min_cost = cost
                    best_medoid = (tx, ty)

            # Output the best medoid coordinates for the current cluster
            print(f"{best_medoid[0]},{best_medoid[1]}")
        
        # Move on to the new medoid and reset the cluster points
        current_medoid = medoid_tuple
        cluster_points = []
    
    # Adding the current trip's dropoff point to the list of cluster points
    cluster_points.append((float(dropoff_x), float(dropoff_y)))

# Processing the last cluster after the loop ends
if current_medoid:
    best_medoid = current_medoid
    min_cost = float('inf')
    
    # Finding the best medoid for the last cluster using the same procedure as above
    for i, (tx, ty) in enumerate(cluster_points):
        cost = sum(euclidean_distance(tx, ty, x, y) for (x, y) in cluster_points)
        if cost < min_cost:
            min_cost = cost
            best_medoid = (tx, ty)

    # Output the best medoid coordinates for the final cluster
    print(f"{best_medoid[0]},{best_medoid[1]}")
