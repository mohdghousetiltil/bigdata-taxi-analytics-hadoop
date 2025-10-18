#!/usr/bin/env python3
import sys

# In-mapper combining: store counts and sums locally before emitting
taxi_data = {}

for line in sys.stdin:
    # Split input line
    trip_id, taxi_num, fare, distance, *_ = line.strip().split(",")
    
    try:
        taxi_num = int(taxi_num)
        fare = float(fare)
        distance = float(distance)
    except ValueError:
        continue  # Skip invalid rows
    
    # Determine trip type
    if distance >= 200:
        trip_type = "long"
    elif distance >= 100:
        trip_type = "medium"
    else:
        trip_type = "short"

    if taxi_num not in taxi_data:
        taxi_data[taxi_num] = {'long': [], 'medium': [], 'short': []}
    
    # Add trip details (fare) to the appropriate trip type
    taxi_data[taxi_num][trip_type].append(fare)

# Emit intermediate results
for taxi_num, trip_info in taxi_data.items():
    for trip_type, fares in trip_info.items():
        if fares:
            count = len(fares)
            max_fare = max(fares)
            min_fare = min(fares)
            avg_fare = sum(fares) / count
            print(f"{taxi_num}\t{trip_type}\t{count}\t{max_fare}\t{min_fare}\t{avg_fare}")
