#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if len(line.split(",")) == 4:

        # Extract the taxi information
        Taxi, company, model, year = line.split(",")
        print(f"{Taxi}\tTAXI,{company}")

    else:
        
        # If the line does not contain 4 values, assume it is trip data
        Trip, Taxi, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = line.split(",")
        print(f"{Taxi}\tTRIP,1")
