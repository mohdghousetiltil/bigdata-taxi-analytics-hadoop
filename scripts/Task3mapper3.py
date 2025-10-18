#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    # Split the line into company and trip count based on the tab separator
    company, trip_cnt = line.split("\t")
    # Convert the trip count from string to integer
    trip_cnt = int(trip_cnt)
    print(f"{trip_cnt}\t{company}")
