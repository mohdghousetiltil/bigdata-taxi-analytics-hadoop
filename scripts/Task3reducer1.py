#!/usr/bin/env python3
import sys

# Initialize variables to keep track of the current taxi ID, company name, and trip count
ctaxi = None
company = None
trip_cnt = 0

# Process each line from standard input
for line in sys.stdin:
    # Strip any leading/trailing whitespace and split the line into Taxi ID and values
    line = line.strip()
    Taxi, values = line.split("\t", 1)
    # Split values into data type and data value
    data_type, data_value = values.split(",", 1)

    # Check if the taxi ID has changed
    if ctaxi and ctaxi != Taxi:
        # If so, print the result for the previous taxi (if a company was set)
        if company:
            print(f"{company}\t{trip_cnt}")
        # Update the current taxi ID and reset company and trip count
        ctaxi = Taxi
        company = None
        trip_cnt = 0

    # Update the current taxi ID
    ctaxi = Taxi

    # Update the company name or trip count based on the data type
    if data_type == "TAXI":
        company = data_value
    elif data_type == "TRIP":
        trip_cnt += int(data_value)

# After the loop ends, print the result for the last taxi (if a company was set)
if company:
    print(f"{company}\t{trip_cnt}")
