#!/usr/bin/env python3
import sys
from collections import defaultdict

# Initialize data structure to hold the results
taxi_trip_data = defaultdict(lambda: {'long': [0, 0, float('-inf'), float('inf'), 0],
                                      'medium': [0, 0, float('-inf'), float('inf'), 0],
                                      'short': [0, 0, float('-inf'), float('inf'), 0]})

for line in sys.stdin:
    taxi_num, trip_type, count, max_fare, min_fare, avg_fare = line.strip().split("\t")
    
    taxi_num = int(taxi_num)
    count = int(count)
    max_fare = float(max_fare)
    min_fare = float(min_fare)
    avg_fare = float(avg_fare)

    taxi_trip_data[taxi_num][trip_type][0] += count
    taxi_trip_data[taxi_num][trip_type][1] += count * avg_fare  # Sum of fares for average calculation
    taxi_trip_data[taxi_num][trip_type][2] = max(taxi_trip_data[taxi_num][trip_type][2], max_fare)
    taxi_trip_data[taxi_num][trip_type][3] = min(taxi_trip_data[taxi_num][trip_type][3], min_fare)

# Emit final result
for taxi_num, trip_info in taxi_trip_data.items():
    for trip_type, values in trip_info.items():
        count, total_fare_sum, max_fare, min_fare, _ = values
        if count > 0:
            avg_fare = total_fare_sum / count
            print(f"{taxi_num}\t{trip_type}\t{count}\t{max_fare}\t{min_fare}\t{avg_fare}")
