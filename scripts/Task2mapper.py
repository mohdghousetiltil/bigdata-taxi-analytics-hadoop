#!/usr/bin/env python3
import sys
import math

# Calculate the Euclidean distance between two points (x1, y1) and (x2, y2)
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Open and read the initialization.txt file to retrieve the number of medoids
with open("initialization.txt", "r") as f:
    lines = f.readlines()
    v = int(lines[0].strip())
    medoids = [tuple(map(float, line.split())) for line in lines[1:]]
# Reading input data
for line in sys.stdin:
    data = line.strip().split(',')
    trip_id = data[0]
    dropoff_x = float(data[-2])
    dropoff_y = float(data[-1])

    # Finding the closest medoid by calculating the Euclidean distance between the dropoff and each medoid
    min_dist = float('inf')
    closest_medoid = None
    for i, (mx, my) in enumerate(medoids):
        dist = euclidean_distance(dropoff_x, dropoff_y, mx, my)
        if dist < min_dist:
            min_dist = dist
            closest_medoid = (mx, my)
    #output
    print(f"{closest_medoid}\t{trip_id},{dropoff_x},{dropoff_y}")
