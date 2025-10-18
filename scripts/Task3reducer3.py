#!/usr/bin/env python3
import sys

# Initialize a list to store tuples of (trip count, company name)
companytlst = []

# Process each line from standard input
for line in sys.stdin:
    # Strip any leading/trailing whitespace and split the line into trip count and company name
    line = line.strip()
    trip_cnt, company = line.split("\t")
    # Convert trip count to an integer
    trip_cnt = int(trip_cnt)
    # Append the tuple (trip count, company name) to the list
    companytlst.append((trip_cnt, company))

# Sort the list of tuples by trip count (ascending order)
companytlst.sort()

# Print each company and its trip count, sorted by trip count
for trip_cnt, company in companytlst:
    print(f"{company}\t{trip_cnt}")
