#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Remove leading and trailing whitespace from the line
    print(line.strip())
