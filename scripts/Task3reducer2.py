#!/usr/bin/env python3
import sys

# Initialize variables to keep track of the current company and the total trip count
ccompany = None
ttl_trips = 0

# Process each line from standard input
for line in sys.stdin:
    # Strip any leading/trailing whitespace and split the line into company and trip count
    line = line.strip()
    company, trip_cnt = line.split("\t")
    # Convert trip count to an integer
    trip_cnt = int(trip_cnt)

    # Check if the company ID has changed
    if ccompany and ccompany != company:
        # If so, print the result for the previous company
        print(f"{ccompany}\t{ttl_trips}")
        # Update the current company and reset the total trip count
        ccompany = company
        ttl_trips = 0

    # Update the current company and add the current trip count to the total
    ccompany = company
    ttl_trips += trip_cnt

# After the loop ends, print the result for the last company (if there is one)
if ccompany:
    print(f"{ccompany}\t{ttl_trips}")
